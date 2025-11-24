from PySide6.QtWidgets import QTableWidget, QMenu, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QCursor

# from public_functions import get_empty_third_dict

from functools import partial
import pickle


def read_only_item(text):
    item = QTableWidgetItem(text)
    item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
    return item


class MTable(QTableWidget):
    signal_delete = Signal(list)    # 一个变量， 由 被删除的行的 id组成的list
    signal_import = Signal()
    signal_export = Signal(list)        # 一个变量， 由 要导出的行组成的list
    signal_new_plot = Signal(list, list, list)     # row ids, labels, types
    signal_add_lines = Signal(list, list, list)    # row ids, labels, types
    signal_column_size_changed = Signal(str, list)
    signal_widget_enabled_during_action = Signal(bool)
    signal_item_text_changed = Signal(str, str, str)     # 第一个变量为id, 第二个为修改列号对应的key name, 第三个为变化后的值

    def __init__(self, parent=None):
        super(MTable, self).__init__(parent)
        self.main_context_menu = None
        self.add_custom_context_menu()
        self.default_sort = [0, Qt.SortOrder.AscendingOrder]
        self.table_name = 'defualt'
        self.horizontalHeader().sectionResized.connect(self.the_columnResized)
        self.itemChanged.connect(self.the_item_changed)
        # self.read_only_item('test')

    def the_item_changed(self, new_item: QTableWidgetItem):
        curr_row = new_item.row()
        curr_col = new_item.column()
        col_ls = ['id', 'time', 'label', 'name', 'type', 'description']
        self.signal_item_text_changed.emit(self.item(curr_row, 0).text(), col_ls[curr_col], new_item.text())

    def the_columnResized(self, column: int, oldWidth: int, newWidth: int):
        col_width_ls = []
        # 只存前六项
        for i in range(6):
            col_width_ls.append(self.columnWidth(i))
        self.signal_column_size_changed.emit(self.table_name, col_width_ls)

    def show_context_menu(self, pos):
        self.main_context_menu.exec(QCursor.pos())

    def add_custom_context_menu(self):
        self.main_context_menu = QMenu()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        action_new_plot = QAction('new plot', parent=self)
        self.main_context_menu.addAction(action_new_plot)

        action_add_lines = QAction('add lines', parent=self)
        self.main_context_menu.addAction(action_add_lines)

        self.main_context_menu.addSeparator()

        action_import = QAction('import', parent=self)
        self.main_context_menu.addAction(action_import)

        # action_export = QAction('export', parent=self)
        # self.main_context_menu.addAction(action_export)

        self.main_context_menu.addSeparator()

        sort_menu = QMenu('sort', self)
        self.main_context_menu.addAction(sort_menu.menuAction())
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

        self.main_context_menu.addSeparator()

        action_delete = QAction('delete', self)
        self.main_context_menu.addAction(action_delete)

        # connect to slot
        action_new_plot.triggered.connect(self.create_plot)
        action_add_lines.triggered.connect(self.add_lines_to_plot)
        action_import.triggered.connect(self.import_datas)
        # action_export.triggered.connect(self.export_datas)
        action_delete.triggered.connect(self.delete_datas)

        # 列序号： id 为0, time为 1, name为 3
        sort_id_ascend.triggered.connect(partial(self.set_table_sort_model, 0, Qt.SortOrder.AscendingOrder))
        sort_id_descend.triggered.connect(partial(self.set_table_sort_model, 0, Qt.SortOrder.DescendingOrder))
        sort_time_ascend.triggered.connect(partial(self.set_table_sort_model, 1, Qt.SortOrder.AscendingOrder))
        sort_time_descend.triggered.connect(partial(self.set_table_sort_model, 1, Qt.SortOrder.DescendingOrder))
        sort_name_ascend.triggered.connect(partial(self.set_table_sort_model, 3, Qt.SortOrder.AscendingOrder))
        sort_name_descend.triggered.connect(partial(self.set_table_sort_model, 3, Qt.SortOrder.DescendingOrder))

    def create_plot(self):
        _, sel_ids, sel_labels, sel_types = self.get_selected_rows()
        self.signal_new_plot.emit(sel_ids, sel_labels, sel_types)

    def add_lines_to_plot(self):
        _, sel_ids, sel_labels, sel_types = self.get_selected_rows()
        self.signal_add_lines.emit(sel_ids, sel_labels, sel_types)

    def import_datas(self):
        self.signal_import.emit()

    # def export_datas(self):
    #     _, sel_ids, _, _1 = self.get_selected_rows()
    #     self.signal_export.emit(sel_ids)

    # 删除行，并发送删除信号
    def delete_datas(self):
        self.signal_widget_enabled_during_action.emit(False)
        sel_rows, sel_ids, _, _1 = self.get_selected_rows()
        sel_rows = sorted(sel_rows, reverse=True)
        ori_n_rows = self.rowCount()
        for row in sel_rows:
            self.removeRow(row)
        # 发送信号，删除对应的文件
        self.setRowCount(ori_n_rows - len(sel_rows))
        self.signal_delete.emit(sel_ids)
        self.signal_widget_enabled_during_action.emit(True)

    # 在切换main/second folder之后，从传入dict来获得表格
    def new_table(self, data_dict, flag_append=False):
        # print(data_dict)
        if flag_append:
            ori_n_rows = self.rowCount()
        else:
            self.clearContents()
            ori_n_rows = 0
        if data_dict is not None:
            ids = data_dict['id']
            times = data_dict['time']
            labels = data_dict['label']
            names = data_dict['name']
            descriptions = data_dict['description']
            data_types = data_dict['type']
            rvalueNames = data_dict['rvalueName']
            new_n_ros = len(ids) + ori_n_rows

            self.setRowCount(new_n_ros)

            # print(ids)
            counts = 0
            for i in range(ori_n_rows, new_n_ros):
                self.setItem(i, 0, read_only_item(ids[counts]))
                self.setItem(i, 1, read_only_item(times[counts]))
                self.setItem(i, 2, QTableWidgetItem(labels[counts]))
                self.setItem(i, 3, QTableWidgetItem(names[counts]))
                self.setItem(i, 4, read_only_item(data_types[counts]))
                self.setItem(i, 5, QTableWidgetItem(descriptions[counts]))
                counts += 1
            cols = 5
            for r_value in range(10):
                if rvalueNames[r_value] is not None:
                    self.setColumnCount(cols)
                    cols += 1
                    head_item = QTableWidgetItem(rvalueNames[r_value])
                    self.setHorizontalHeaderItem(cols, head_item)
                    temp_values = data_dict[f'rvalue{r_value}']
                    counts = 0
                    for i in range(ori_n_rows, new_n_ros):
                        self.setItem(i, cols, read_only_item(temp_values[counts]))
                        counts += 1
        self.sort_tables()

    # # new table 反过来，由table 获取dict
    # def get_dict_from_table(self):
    #     tb_dict = get_empty_third_dict()
    #     if self.columnCount() == 0:
    #         return None
    #     for i in range(self.rowCount()):
    #         tb_dict['id'].append(self.item(i, 0).text())
    #         tb_dict['time'].append(self.item(i, 1).text())
    #         tb_dict['label'].append(self.item(i, 2).text())
    #         tb_dict['name'].append(self.item(i, 3).text())
    #         tb_dict['type'].append(self.item(i, 4).text())
    #         tb_dict['description'].append(self.item(i, 5).text())
    #     return tb_dict

    # 获取被选中的行数
    def get_selected_rows(self):
        sel_ids = []
        sel_rows = []
        sel_labels = []
        sel_types = []
        try:
            sel_index = self.selectedIndexes()
            for i in sel_index:
                row = i.row()
                sel_rows.append(row)
                sel_ids.append(self.item(row, 0).text())
                sel_labels.append(self.item(row, 2).text())
                sel_types.append(self.item(row, 4).text())
        except Exception as e:
            print(e)
            sel_rows = []
            sel_ids = []
        return [sel_rows, sel_ids, sel_labels, sel_types]

    # 设置默认的排序方式，并排序
    def set_table_sort_model(self, col, order):
        self.default_sort = [col, order]
        self.sort_tables()

    # 按默认的排序方式排序
    def sort_tables(self):
        self.sortItems(self.default_sort[0], self.default_sort[1])

