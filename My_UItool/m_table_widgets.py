from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMenu
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QBrush, QAction, QCursor
import pickle
from functools import partial

from My_UItool.m_table_widget_item import BaseTableItem, item_dict, FloatItem
from pandas import DataFrame

flag_in_debug = True


class BaseTable(QTableWidget):
    """
    must run the "init_table" function before use the table,

    tool functions:
        insert_row(index: INT, row_items: [(), ()]): 插入到index 位置
        delete_row(index):
        append_rows(row_items: []):
        copy_row(index_ls):
        paste_row(index):

        get_table_content(): 获取表格所有值，
    protect function:
        _get_row_content_by_index(index): 获取index行的内部，返回tuple类型
        _set_read_only_columns([bool list]): 输入参数为bool list,长度与表格列数相等，read only的列为True，不是的为False
    param:
        clipboard
    """

    def __init__(self, parent=None):
        super(BaseTable, self).__init__(parent=parent)

        # self.bg_color_error = QBrush(color=Qt.GlobalColor.red)
        # self.bg_color_normal = QBrush(color=Qt.GlobalColor.white)
        # self.bg_color_run = QBrush(color=Qt.GlobalColor.green)
        self.clipboard = []
        self.file_path_size_pos = None
        self.n_columns = 0
        self.n_rows = 0
        self.column_width_ls = []
        self.horizontalHeader().sectionResized.connect(self.header_section_resized)
        self.itemChanged.connect(self.slot_item_changed)
        self.NewItem_ls = []
        self.column_default = []
        self.column_read_only = ()

    def slot_item_changed(self, item: BaseTableItem):
        item.item_text_changed()

    def init_table(self, tb_name, columns: dict, read_only_tuple=None):
        """

        :param tb_name:
        :param columns:  {column_name: (column_type, default_name)}
        :param read_only_tuple:
        :return:
        """
        self.file_path_size_pos = f'.systems/size_and_pos/{tb_name}_size_pos.pkl'
        n_columns = len(columns)
        self.n_columns = n_columns
        self.setColumnCount(n_columns)
        if read_only_tuple is None:
            self.column_read_only = tuple([False for _ in range(n_columns)])
        else:
            if len(read_only_tuple) != n_columns:
                raise ValueError('the length of "read only ls" is not equal the number of columns')
            self.column_read_only = read_only_tuple

        flag_load_column_width_succeed = False
        try:
            with open(self.file_path_size_pos, 'rb') as file:
                col_width_ls = pickle.load(file)
                if len(col_width_ls) == n_columns:
                    self.column_width_ls = col_width_ls
                    flag_load_column_width_succeed = True
        except FileNotFoundError:
            pass

        col_default = []

        i_col = 0
        for item in columns.items():
            col_name = item[0]
            col_type, default_value = item[1]
            self.NewItem_ls.append(item_dict[col_type])
            col_default.append(default_value)

            # set heater item
            temp_heater_item = QTableWidgetItem(col_name)
            self.setHorizontalHeaderItem(i_col, temp_heater_item)

            # set the column width
            if flag_load_column_width_succeed:
                # if load succeed, init the column widths with the data from pkl
                self.setColumnWidth(i_col, self.column_width_ls[i_col])
            else:
                # if load failed, get the current column width data
                self.column_width_ls.append(self.columnWidth(i_col))
            i_col += 1
        self.column_default = [tuple(col_default)]

    def header_section_resized(self, logical_index, old_size, new_size):
        self.column_width_ls[logical_index] = new_size
        with open(self.file_path_size_pos, 'wb') as file:
            pickle.dump(self.column_width_ls, file)

    def append_row_into_table(self, rows_ls: list):
        """
        在表格最后，插入一行或多行
        :param rows_ls: 插入的行数, list变量，元素为tuple. tuple的长度应与表格列数一致
        :return: None
        """
        self.insert_rows_into_table(self.n_rows, rows_ls)

    def df_to_table(self, df: DataFrame):
        self.clearContents()
        n_df = len(df)
        self.setRowCount(n_df)

        i_count = -1
        for i_row in df.index:
            i_count += 1
            row_data = df.loc[i_row]
            j = -1
            for data in row_data:
                j += 1
                self.setItem(i_count, j, FloatItem(data, True))
            # for j in range(n_vars):
            #     # temp_str = f"{df.loc[i][j]:.8g}"

    def new_table_with_rows(self, rows_ls: list):
        self.clearContents()
        self.setRowCount(0)
        self.n_rows = 0
        self.insert_rows_into_table(self.n_rows, rows_ls)

    def insert_rows_into_table(self, row_index, rows_ls):
        """
        插入行
        :param rows_ls:
        :param row_index:  插入到第index行
        :return:
        """
        n_new_rows = len(rows_ls)
        # 插入的行数为零则返回
        if n_new_rows == 0:
            return
        # 从index，逐行输入row ls
        for row_tuple in rows_ls:
            if len(row_tuple) != self.n_columns:
                continue
            self.insertRow(row_index)
            for i_col in range(self.n_columns):
                TempObj = self.NewItem_ls[i_col]
                self.setItem(row_index, i_col, TempObj(row_tuple[i_col], self.column_read_only[i_col]))
            row_index += 1
        self.n_rows = self.rowCount()

    def get_selected_row_content(self):
        sel_row = self._get_select_row_index()
        res = []
        for i_row in sel_row:
            res.append(self._get_row_content_by_index(i_row))
        return res

    def get_table_content(self):
        res = []
        for i in range(self.n_rows):
            res.append(self._get_row_content_by_index(i))
        return res

    def _get_row_content_by_index(self, i_row):
        row_content = []

        if (i_row < 0) or (i_row > self.n_rows):
            raise ValueError("Invalid row index")
        for i_col in range(self.n_columns):
            temp_item: BaseTableItem = self.item(i_row, i_col)
            row_content.append(temp_item.get_value())
        return tuple(row_content)

    def _get_select_row_index(self):
        sel_rows = []
        try:
            sel_indexes = self.selectedIndexes()
            for sel_i in sel_indexes:
                row = sel_i.row()
                sel_rows.append(row)
        except Exception as e:
            print(e)
            sel_rows = []
        return sel_rows

    # slot action for mouse triggered signal
    def slot_delete_sel_rows_from_table(self):
        sel_rows = self._get_select_row_index()
        # 从大到小排序
        sel_rows = sorted(sel_rows, reverse=True)
        # 从后面的行开始删除，避免删除过程中行号变化的问题
        for row in sel_rows:
            self.removeRow(row)
        # 更新 row counts
        self.n_rows = self.n_rows - len(sel_rows)
        self.setRowCount(self.n_rows)

    # slot action for mouse triggered signal
    def slot_copy_sel_rows_to_clipboard(self):
        self.clipboard = self.get_selected_row_content()

    # slot action for mouse triggered signal
    def slot_paste_to_sel_rows_from_clipboard(self):
        sel_rows = self._get_select_row_index()
        if len(sel_rows) == 0:
            return
        else:
            i_row = sel_rows[0] + 1
        if len(self.clipboard) > 0:
            clip_board = self.clipboard[:]
            self.insert_rows_into_table(i_row, clip_board)

    def slot_change_table_content(self, i_row, i_col, new_text:str):
        temp_item = self.item(i_row, i_col)
        if (new_text != '') and (new_text is not None):
            temp_item.setText(new_text)

    # slot action for mouse triggered signal
    def insert_row_before_sel(self, default_var_ls=None):
        sel_rows = self._get_select_row_index()
        if len(sel_rows) == 0:
            return
        i_first_row = sel_rows[0]
        self.insert_rows_into_table(i_first_row, [self._get_row_content_by_index(i_first_row)])
        self.__set_item_value(i_first_row, default_var_ls)

    def change_row_sel(self, default_var_ls=None):
        sel_rows = self._get_select_row_index()
        if len(sel_rows) == 0:
            return
        i_first_row = sel_rows[0]
        self.__set_item_value(i_first_row, default_var_ls)

    # slot action for mouse triggered signal
    def insert_row_after_sel(self, default_var_ls=None):
        sel_rows = self._get_select_row_index()
        if len(sel_rows) == 0:
            return
        i_last_row = sel_rows[-1]
        self.insert_rows_into_table(i_last_row+1, [self._get_row_content_by_index(i_last_row)])
        self.__set_item_value(i_last_row+1, default_var_ls)

    # slot action for mouse triggered signal
    def append_row_at_last(self, default_var_ls=None):
        self.insert_rows_into_table(self.n_rows, self.column_default)
        self.__set_item_value(self.n_rows-1, default_var_ls)

    def __set_item_value(self, i_row, default_var_ls=None):
        if default_var_ls is None:
            return
        for val_tuple in default_var_ls:
            col = val_tuple[0]
            self.item(i_row, col).setText(str(val_tuple[1]))

    # function for debug
    def show_table_content(self):
        res = self.get_table_content()
        for row in res:
            print(row)


class RecipeTable(BaseTable):

    def __init__(self, parent=None):
        super(RecipeTable, self).__init__(parent=parent)
        self.init_table(tb_name='recipe_table',
                        columns={
                            'Instr': ('TEXT NOT NULL', 'time'),
                            'Source': ('TEXT NOT NULL', 'time'),
                            'Goals': ('FLOAT', 0),
                            'Steps': ('FLOAT', 0.1),
                            'RampSpeed': ('FLOAT', 0.1),
                            'PauseTime': ('FLOAT', 1),
                            'Plot': ('BOOL', True),
                        }, read_only_tuple=(True, True, False, False, False, False, False))
        # self.append_row_into_table([('time', 'time', 1, 0.1, 0.1, 1, True)])
        # self.append_row_into_table([('time', 'time', 2, 0.1, 0.1, 1, True)])
        # self.insert_rows_into_table(0, [('time', 'time', 0, 0.1, 0.1, 1, False)])

        self.output_channels = {}
        self.main_context_menu = None

    def get_output_function(self, k1, k2):
        return self.output_channels[(k1, k2)]

    # debug function
    def show_all_outp_function(self):
        res = self.get_table_content()
        for temp_tuple in res:
            print(self.get_output_function(temp_tuple[0], temp_tuple[1]))

    def show_context_menu(self, pos):
        self.main_context_menu.exec(QCursor.pos())

    def set_main_context_menu(self, output_channels):
        self.output_channels = output_channels

        self.main_context_menu = QMenu()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        menu_insert_before = QMenu('insert before', self)
        self.set_sub_context_menu('insert before', menu_insert_before, output_channels)
        self.main_context_menu.addAction(menu_insert_before.menuAction())

        menu_apply_change = QMenu('change row', self)
        self.set_sub_context_menu('apply change', menu_apply_change, output_channels)
        self.main_context_menu.addAction(menu_apply_change.menuAction())

        menu_insert_after = QMenu('insert after', self)
        self.set_sub_context_menu('insert after', menu_insert_after, output_channels)
        self.main_context_menu.addAction(menu_insert_after.menuAction())

        menu_append = QMenu('append at last', self)
        self.set_sub_context_menu('append', menu_append, output_channels)
        self.main_context_menu.addAction(menu_append.menuAction())

        self.main_context_menu.addSeparator()

        act_copy = QAction('copy', self)
        act_paste = QAction('paste', self)
        self.main_context_menu.addAction(act_copy)
        self.main_context_menu.addAction(act_paste)

        act_copy.triggered.connect(self.slot_copy_sel_rows_to_clipboard)
        act_paste.triggered.connect(self.slot_paste_to_sel_rows_from_clipboard)

        self.main_context_menu.addSeparator()

        act_delete = QAction('delete', self)
        self.main_context_menu.addAction(act_delete)
        act_delete.triggered.connect(self.slot_delete_sel_rows_from_table)

        if flag_in_debug:
            act_show_table_content = QAction('show content', self)
            self.main_context_menu.addAction(act_show_table_content)
            act_show_table_content.triggered.connect(self.show_table_content)

            act_show_all_function = QAction('show func', self)
            self.main_context_menu.addAction(act_show_all_function)
            act_show_all_function.triggered.connect(self.show_all_outp_function)

    def set_sub_context_menu(self, call_action: str, menu: QMenu, output_channels: list):
        if call_action == 'insert before':
            temp_fun = self.insert_row_before_sel
        elif call_action == 'insert after':
            temp_fun = self.insert_row_after_sel
        elif call_action == 'append':
            temp_fun = self.append_row_at_last
        elif call_action == 'apply change':
            temp_fun = self.change_row_sel
        else:
            return

        for item in output_channels:
            k1, k2 = item
            temp_action = QAction(f"{k1} : {k2}", self)
            menu.addAction(temp_action)
            temp_action.triggered.connect(partial(temp_fun, [(0, k1), (1, k2)]))


class CustomTable(BaseTable):

    def __init__(self, parent=None):
        super(CustomTable, self).__init__(parent=parent)
        self.init_table(tb_name='custom_table',
                        columns={
                            'name': ('TEXT NOT NULL', 'custom1'),
                            'Expection': ('TEXT NOT NULL', '1')
                        })
        # self.append_row_into_table([('custom1', 1)])
        self.set_action_menu()

    def set_action_menu(self):
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)

        act_insert_before = QAction('insert before', self)
        act_insert_after = QAction('insert after', self)
        act_append = QAction('append at last', self)
        self.addAction(act_insert_before)
        self.addAction(act_insert_after)
        self.addAction(act_append)

        separator1 = QAction(self)
        separator1.setSeparator(True)
        self.addAction(separator1)

        act_copy = QAction('copy', self)
        act_paste = QAction('paste', self)
        self.addAction(act_copy)
        self.addAction(act_paste)

        separator2 = QAction(self)
        separator2.setSeparator(True)
        self.addAction(separator2)

        act_delete = QAction('delete', self)
        self.addAction(act_delete)

        act_insert_before.triggered.connect(partial(self.insert_row_before_sel, None))
        act_insert_after.triggered.connect(partial(self.insert_row_after_sel, None))
        act_append.triggered.connect(partial(self.append_row_at_last, None))

        act_copy.triggered.connect(self.slot_copy_sel_rows_to_clipboard)
        act_paste.triggered.connect(self.slot_paste_to_sel_rows_from_clipboard)

        act_delete.triggered.connect(self.slot_delete_sel_rows_from_table)

        if flag_in_debug:
            act_show_table_content = QAction('show content', self)
            self.addAction(act_show_table_content)
            act_show_table_content.triggered.connect(self.show_table_content)


# dataset下的子table，展示数据库内已经跑过的程序
class RunTable(BaseTable):
    signal_table_item_changed = Signal(str, str, tuple)     # tb_name, row index, col name, tuple(new values)
    signal_view_data = Signal(list, list)  # table name, run_name_ls
    signal_export_data = Signal(list, list)     # 导出
    signal_move_to = Signal(list, int)     # 数据移动到其他dataset, tb_name_ls, goal_ds_id
    signal_copy_to = Signal(list, int)  # 数据移动到其他dataset, tb_name_ls, goal_ds_id
    signal_concat_to = Signal(list, int)
    signal_delete = Signal(list)
    signal_new_plot = Signal(list, list, list)
    signal_add_plot = Signal(list, list, list)
    signal_send_to_analysis = Signal(list, list, str)

    def __init__(self, parent=None):
        super(RunTable, self).__init__(parent=parent)
        self.init_table(tb_name='DataSet_run_table',
                        columns={
                            'table_id': ('TEXT NOT NULL', 'table_00001'),
                            'time': ('TEXT', '23-3-24-def_time'),
                            'label': ('TEXT NOT NULL', 'default label'),
                            'run_name': ('TEXT NOT NULL', 'label1'),
                            'type': ('TEXT', '2d'),
                            'description': ('TEXT NOT NULL', 'no description'),
                            'independent_value': ('TEXT', 'x')
                        }, read_only_tuple=(True, True, False, False, True, False, True))
        self.column_names = ('table_id', 'time', 'label', 'run_name', 'type',  'description', 'independent_value')
        self.default_sort = [0, Qt.SortOrder.AscendingOrder]  # 默认按时间排序
        self.sort_tables()
        self.move_to_menu = QMenu('move to', self)
        self.copy_to_menu = QMenu('copy to', self)
        self.concat_to_menu = QMenu('concat to', self)
        self.set_action_menu()

    def set_action_menu(self):
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        separator = QAction('', self)
        separator.setSeparator(True)

        action_new_plot = QAction('new plot', parent=self)
        self.addAction(action_new_plot)
        action_new_plot.triggered.connect(partial(self.slot_plot_triggered, 'new'))

        action_add_plot = QAction('add plot', parent=self)
        self.addAction(action_add_plot)
        action_add_plot.triggered.connect(partial(self.slot_plot_triggered, 'add'))

        act_view_datas = QAction('view datas', self)
        self.addAction(act_view_datas)
        act_view_datas.triggered.connect(partial(self.get_sel_tb_name, 'view'))

        separator = QAction('', self)
        separator.setSeparator(True)
        self.addAction(separator)

        sort_menu = QMenu('sort', self)
        self.addAction(sort_menu.menuAction())
        sort_name_ascend = QAction('name ↑', self)
        sort_name_descend = QAction('name ↓', self)
        sort_id_ascend = QAction('id ↑', self)
        sort_id_descend = QAction('id ↓', self)
        sort_time_ascend = QAction('time ↑', self)
        sort_time_descend = QAction('time ↓', self)
        sort_menu.addAction(sort_id_ascend)
        sort_menu.addAction(sort_id_descend)
        sort_menu.addSeparator()
        sort_menu.addAction(sort_time_ascend)
        sort_menu.addAction(sort_time_descend)
        sort_menu.addSeparator()
        sort_menu.addAction(sort_name_ascend)
        sort_menu.addAction(sort_name_descend)
        sort_id_ascend.triggered.connect(partial(self.set_table_sort_model, 0, Qt.SortOrder.AscendingOrder))
        sort_id_descend.triggered.connect(partial(self.set_table_sort_model, 0, Qt.SortOrder.DescendingOrder))
        sort_time_ascend.triggered.connect(partial(self.set_table_sort_model, 1, Qt.SortOrder.AscendingOrder))
        sort_time_descend.triggered.connect(partial(self.set_table_sort_model, 1, Qt.SortOrder.DescendingOrder))
        sort_name_ascend.triggered.connect(partial(self.set_table_sort_model, 3, Qt.SortOrder.AscendingOrder))
        sort_name_descend.triggered.connect(partial(self.set_table_sort_model, 3, Qt.SortOrder.DescendingOrder))

        separator = QAction('', self)
        separator.setSeparator(True)
        self.addAction(separator)

        send_menu = QMenu('send to Analysis', self)
        self.addAction(send_menu.menuAction())

        act_hall_mobility = QAction('hall mobility', self)
        send_menu.addAction(act_hall_mobility)
        act_hall_mobility.triggered.connect(partial(self.sent_to_analysis, 'hall mobility'))

        act_magnet_resist_analysis = QAction('magnet resist analysis', self)
        send_menu.addAction(act_magnet_resist_analysis)
        act_magnet_resist_analysis.triggered.connect(partial(self.sent_to_analysis, 'magnet resist analysis'))

        act_fet_mobility = QAction('FET mobility', self)
        send_menu.addAction(act_fet_mobility)
        act_fet_mobility.triggered.connect(partial(self.sent_to_analysis, 'FET mobility'))

        separator = QAction('', self)
        separator.setSeparator(True)
        self.addAction(separator)

        act_export_datas = QAction('export datas', self)
        self.addAction(act_export_datas)
        act_export_datas.triggered.connect(partial(self.get_sel_tb_name, 'export'))

        separator = QAction('', self)
        separator.setSeparator(True)
        self.addAction(separator)

        act_delete = QAction('delete copy or concat datas', self)
        self.addAction(act_delete)
        act_delete.triggered.connect(partial(self.get_sel_tb_name, 'delete'))

        separator = QAction('', self)
        separator.setSeparator(True)
        self.addAction(separator)

        # move to
        self.addAction(self.move_to_menu.menuAction())
        self.addAction(self.copy_to_menu.menuAction())

        separator = QAction('', self)
        separator.setSeparator(True)
        self.addAction(separator)

        self.addAction(self.concat_to_menu.menuAction())

    def sent_to_analysis(self, fun):
        tb_content = self.get_selected_row_content()
        tb_name_ls = []
        run_name_ls = []

        for row in tb_content:
            tb_name_ls.append(row[0])
            run_name_ls.append(row[3])
        self.signal_send_to_analysis.emit(tb_name_ls, run_name_ls, fun)

    def set_move_to_menu(self, data_set_name, data_set_id):
        self.move_to_menu.clear()
        self.copy_to_menu.clear()
        self.concat_to_menu.clear()

        count = 0
        for name in data_set_name:
            temp_act = QAction(name, self)
            temp_act.triggered.connect(partial(self.slot_move_to_triggered, data_set_id[count]))
            self.move_to_menu.addAction(temp_act)

            temp_act2 = QAction(name, self)
            temp_act2.triggered.connect(partial(self.slot_copy_to_triggered, data_set_id[count]))
            self.copy_to_menu.addAction(temp_act2)

            temp_act3 = QAction(name, self)
            temp_act3.triggered.connect(partial(self.slot_concat_to_triggered, data_set_id[count]))
            self.concat_to_menu.addAction(temp_act3)
            count += 1

    def slot_plot_triggered(self, flag: str):
        tb_content = self.get_selected_row_content()
        tb_name_ls = []
        tb_label_ls = []
        tb_type_ls = []
        for row in tb_content:
            tb_name_ls.append(row[0])
            tb_label_ls.append(row[2])
            tb_type_ls.append(row[4])
        if flag == 'new':
            self.signal_new_plot.emit(tb_name_ls, tb_label_ls, tb_type_ls)
        elif flag == 'add':
            self.signal_add_plot.emit(tb_name_ls, tb_label_ls, tb_type_ls)

    def slot_move_to_triggered(self, goal_dataset_id):
        tb_content = self.get_selected_row_content()
        tb_name_ls = []
        for row in tb_content:
            tb_name_ls.append(row[0])
        if len(tb_name_ls) > 0:
            self.signal_move_to.emit(tb_name_ls, goal_dataset_id)

    def slot_copy_to_triggered(self, goal_dataset_id):
        tb_content = self.get_selected_row_content()
        tb_name_ls = []
        for row in tb_content:
            tb_name_ls.append(row[0])
        if len(tb_name_ls) > 0:
            self.signal_copy_to.emit(tb_name_ls, goal_dataset_id)

    def slot_concat_to_triggered(self, goal_dataset_id):
        tb_content = self.get_selected_row_content()
        tb_name_ls = []
        for row in tb_content:
            tb_name_ls.append(row[0])
        if len(tb_name_ls) > 0:
            self.signal_concat_to.emit(tb_name_ls, goal_dataset_id)

    def get_sel_tb_name(self, caller):
        tb_content = self.get_selected_row_content()
        # print(tb_content)
        tb_name_ls = []
        label_ls = []
        run_name_ls = []
        for row in tb_content:
            tb_name_ls.append(row[0])
            label_ls.append(row[2])
            run_name_ls.append(row[3])

        if len(tb_name_ls) > 0:
            if caller == 'view':
                self.signal_view_data.emit(tb_name_ls, run_name_ls)
            elif caller == 'export':
                self.signal_export_data.emit(tb_name_ls, label_ls)
            elif caller == 'delete':
                self.signal_delete.emit(tb_name_ls)

    def slot_item_changed(self, item: BaseTableItem):
        res = item.item_text_changed()
        c_row = item.row()
        tb_name = self.item(c_row, 0).text()
        col_name = self.column_names[item.column()]

        if res:
            self.signal_table_item_changed.emit(tb_name, col_name, (item.get_value()))

    # 设置默认的排序方式，并排序
    def set_table_sort_model(self, col, order):
        self.default_sort = (col, order)
        self.sort_tables()

    # 按默认的排序方式排序
    def sort_tables(self):
        self.sortItems(self.default_sort[0], self.default_sort[1])


