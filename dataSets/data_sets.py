import sqlite3
import threading
from datetime import datetime


def load_or_create_database(database_path):
    database_manager = DatabaseManager(database_path=database_path)
    return database_manager


class DatabaseManager:

    def __init__(self, database_path):
        self.db_path = database_path
        self.present_data_set_id = 0
        self.present_run_id = 0
        self.run_table_name = 'table_00001'
        self.dm_cursor = DataBaseConnector()
        self._set_new_database_path(database_path)

    def get_all_run_table_records(self):
        # with self._connect:
        #     res = self._connect.sql_query('SELECT * FROM runTable')
        #     col_name_ls = tuple(t[0] for t in self._connect.cursor.description)
        #     tb_ls = [col_name_ls]
        #     for tb_tuple in res:
        #         tb_ls.append(tb_tuple)
        #     return tb_ls
        with self.dm_cursor:
            return self.__get_all_records_from_table('runTable')

    def get_dataset_run_table_records(self, dataset_id: int):
        with self.dm_cursor:
            # res = self._connect.sql_query(f'SELECT * FROM runTable WHERE dataSet = {dataset_id}')
            res = self._select_table(table_name='runTable',
                                     name_ls=('table_id', 'time', 'label', 'run_name',
                                              'type', 'description', 'independent_value'),
                                     condition=f"dataSet = {dataset_id}")
        return res

    def get_run_table_value(self, run_tb_name: str):
        """
        1. 判断run table 是否存在，若不存在，返回None
        若存在，
        2. 返回对应run table 的所有值 [列名， 值1, 值2, ...]
        :param run_tb_name:
        :return:
        """
        if 'c' in run_tb_name:
            run_tb_name = run_tb_name.split('c')[0]

        with self.dm_cursor:
            # 判断run table 是否存在，若不存在，返回None
            table_id = self._select_table(table_name='runTable', name_ls=('table_id', ))
            tb_name_ls = [i[0] for i in table_id]
            if run_tb_name in tb_name_ls:
                return self.__get_all_records_from_table(run_tb_name)
            else:
                return None

    def __get_all_records_from_table(self, table_name):
        f"""
        select all records from the {table_name}
        :param table_name: 
        :return: 
        """
        res = self.dm_cursor.sql_query(f'SELECT * FROM {table_name}')
        col_name_ls = tuple(t[0] for t in self.dm_cursor.cursor.description)
        tb_ls = [col_name_ls]
        for tb_tuple in res:
            tb_ls.append(tb_tuple)
        return tb_ls

    def get_max_run_table_id(self, table_name):
        """
        get the max id of the run table
        :param table_name: name of the run table
        :return: max table id
        """
        with self.dm_cursor:
            res = self._select_table(table_name=table_name, name_ls=('MAX(id)',))
            return res[0][0]

    # 独立线程调用
    # connect during recipe
    def append_rows_to_value_table(self, table_name, var_row_ls: list, var_name_tuple=None):
        """
        append measuring datas into the database
        :param table_name:
        :param var_row_ls:
        :param var_name_tuple:
        :return:
        """
        # with self.dm_cursor:
        for var_ls in var_row_ls:
            self.__insert_without_commit(table_name, var_ls, var_name_tuple)
        self.dm_cursor.commit()

    def get_axes_setting_from_plot_table(self, run_table_name):
        temp_name_tuple = ['axes_num' for i in range(28)]
        for i in range(9):
            temp_name_tuple[i + 1] = f"x{i + 1}"
            temp_name_tuple[i + 10] = f"y{i + 1}"
            temp_name_tuple[i + 19] = f"z{i + 1}"
        temp_name_tuple = tuple(temp_name_tuple)

        with self.dm_cursor:
            res = self._select_table(table_name='plotSettingTable', name_ls=temp_name_tuple,
                                     condition=f"table_id = '{run_table_name}'")
        return res

    def update_rows_of_plot_table(self, table_name_ls: list, axes_setting: list):
        """
        # update
        :param table_name_ls: list of run table name
        :param axes_setting:  list axes_setting [axes_num, x1, x2,... x9, y1, y2, ... y9, z1, z2, ... z9]
        :return:
        """
        u_dict = {'axes_num': axes_setting[0]}
        temp_name_tuple = ['axes_num' for i in range(28)]
        for i in range(9):
            u_dict[f"x{i + 1}"] = axes_setting[i + 1]
            u_dict[f"y{i + 1}"] = axes_setting[i + 10]
            u_dict[f"z{i + 1}"] = axes_setting[i + 19]
            temp_name_tuple[i + 1] = f"x{i + 1}"
            temp_name_tuple[i + 10] = f"y{i + 1}"
            temp_name_tuple[i + 19] = f"z{i + 1}"
        temp_name_tuple = tuple(temp_name_tuple)
        with self.dm_cursor:
            for run_table_name in table_name_ls:
                res = self._select_table(table_name='plotSettingTable', name_ls=temp_name_tuple,
                                         condition=f"table_id = '{run_table_name}'")
                if len(res) == 0:
                    insert_value = [run_table_name] + axes_setting
                    self.__insert_without_commit(table_name='plotSettingTable',
                                                 value_tuple=tuple(insert_value))
                else:
                    self._update_table(table_name='plotSettingTable', var_dict=u_dict,
                                       condition=f"table_id = '{run_table_name}'")
            self.dm_cursor.commit()

    def append_rows_to_plot_table(self, table_name_ls: list, axes_setting: list):
        """
        # insert
        :param table_name_ls: list of run table name
        :param axes_setting:  list axes_setting [axes_num, x1, x2,... x9, y1, y2, ... y9, z1, z2, ... z9]
        :return:
        """
        with self.dm_cursor:
            for run_table_name in table_name_ls:
                insert_value = [run_table_name] + axes_setting
                self.__insert_without_commit(table_name='plotSettingTable',
                                             value_tuple=tuple(insert_value))
            self.dm_cursor.commit()

    # connect during recipe
    def create_value_table(self, index_ls, var_name_ls, plot_legend, run_name, recipe_type, description,
                           independent_vars, dataset_id=None):
        """
        在测量程序开始之前，先创建保存数据的列表（以下简称数表）。创建分以下步骤：
            1. 获取最大的run id, 用于生成数表名
            2. 创建数表
            3. 在run table中添加记录
            4. 更新 maxIdTable
        :param dataset_id:
        :param description: 数表描述
        :param recipe_type: 数表类型， 2d recipe, mapping recipe
        :param plot_legend: 画图，图例
        :param run_name:  seq name
        :param index_ls:  数表索引，list格式， 对于2d recipe， index变量只有一个元素，mapping recipe有三个元素 main index, 一级 二级 Index。 储存格式为int
        :param var_name_ls: 数表变量列表， 储存格式为float
        :param independent_vars: 自变量列表， list格式
        :return: 如果创建成功 返回 table name, 否则 返回 None
        """
        flag_succeed = True
        with self.dm_cursor:
            file_index = self._select_table(table_name='maxIdTable', name_ls=('runId',), condition='id = 0')
            self.present_run_id = file_index[0][0]

            self.present_run_id += 1
            self.run_table_name = f'Table_{self.present_run_id:05d}'

            # 创建数表
            columns = {}
            i = 0
            for index in index_ls:
                if i == 0:
                    columns[index] = 'INT'
                else:
                    columns[index] = 'INT'
                i += 1

            columns['recipe_time'] = 'DOUBLE'
            columns['seqs_time'] = 'DOUBLE'

            # 先更新 maxIdTable
            self._update_table(table_name='maxIdTable',
                               var_dict={'runId': self.present_run_id},
                               condition='id = 0')

            # 先在run table中添加记录
            _independent = ' , '.join(i for i in independent_vars)
            if dataset_id is None:
                dataset_id = self.present_data_set_id
            self._insert_table(table_name='runTable',
                               value_tuple=(dataset_id, self.run_table_name,
                                            datetime.now().strftime("%Y/%m/%d %H:%M:%S"), plot_legend, run_name,
                                            recipe_type, description, _independent))
            for var in var_name_ls:
                columns[var] = 'DOUBLE'
            self._create_table_if_not_exists(table_name=self.run_table_name, columns=columns, key_column=0)

        if flag_succeed:
            return self.run_table_name
        else:
            return None

    def _create_table_if_not_exists(self, table_name: str, columns: dict, key_column: int = 0):
        if key_column >= len(columns) or key_column < 0:
            raise IndexError("主键索引异常")

        column_code = []
        i = 0
        for item in columns.items():
            temp_column = ' '.join(i for i in item)
            if i == key_column:
                column_code.append(f'{temp_column} PRIMARY KEY')
            else:
                column_code.append(temp_column)
            i += 1

        column_code = ', '.join(i for i in column_code)

        sql_code = f'CREATE TABLE IF NOT EXISTS {table_name} ( {column_code} )'

        self.dm_cursor.sql_write(sql_code)

    def create_data_set(self, new_dataset_name):
        """
            1. 从data set table中查找， data_set_name是否已经存在, 如果存在， 返回None，
        如果不存在：
            2. 获取最大的data set id, 用于生成新的data set id, 并将该 id 赋值给当前 data set
            3. 在data set table中添加记录
            4. 更新 maxIdTable
        :param new_dataset_name: data set 的 名字
        :return: 如果创建成功 返回 data set id, 否则（记录已存在）返回 None
        """
        with self.dm_cursor:
            _, dataset_name_ls = self._select_all_records_in_dataset_table()
            if new_dataset_name in dataset_name_ls:
                return None
            else:
                file_index = self._select_table(table_name='maxIdTable', name_ls=('runSetId',), condition='id = 0')
                new_id = file_index[0][0] + 1

                # 在data set table中添加记录
                self._insert_table(table_name='dataSetTable', value_tuple=(new_id, new_dataset_name))

                # 更新 maxIdTable
                self._update_table(table_name='maxIdTable',
                                   var_dict={'runSetId': new_id},
                                   condition='id = 0')
                return new_id

    # 独立线程调用
    # 线程开启cursor
    def change_run_table_records(self, run_table_id, col_name, new_value):
        """

        :param run_table_id: run table id, 用于定位需要修改的行
        :param col_name: values name， 待修改的列名
        :param new_value:
        :return:
        """
        self._update_table(table_name='runTable',
                           var_dict={col_name: new_value}, condition=f"table_id = '{run_table_id}'")

    # 把数据表移动到新的data set 下
    def update_runtable_dataset(self, table_name_ls: list, new_ds_id: int):
        """
        1. 检查
        :param table_name_ls: 要移动的表名
        :param new_ds_id: 目标data set id
        :return:
        """
        # 1 检查 new_ds_id 是否存在
        with self.dm_cursor:
            dataset_id_ls, _ = self._select_all_records_in_dataset_table()
            if new_ds_id not in dataset_id_ls:
                print(f"{new_ds_id} dose not exit")
                return
            for tb_id in table_name_ls:
                self._update_table(table_name='runTable', var_dict={'dataSet': new_ds_id},
                                   condition=f"table_id = '{tb_id}'")

    def change_data_set_name(self, data_set_id, new_dataset_name):
        '''
        改变data set 对应的名字
        1. 判断名字是否存在，如果名字已存在，返回None，如果不存在：则改名，并返回新名字
        :param data_set_id: 要改名的id
        :param new_dataset_name: 新名字
        :return:
        '''
        with self.dm_cursor:
            dataset_id_ls, dataset_name_ls = self._select_all_records_in_dataset_table()
            # 判断new data set name 是否存在
            if new_dataset_name in dataset_name_ls:
                return None
            # 判断data set id 是否存在
            if data_set_id in dataset_id_ls:
                self._update_table(table_name='dataSetTable',
                                   var_dict={'name': new_dataset_name}, condition=f'id = {data_set_id}')

                # self.present_data_set_id = data_set_id
                res = self._select_table(table_name='dataSetTable', name_ls=('name',), condition=f'id = {data_set_id}')
                return res[0][0]
            else:
                return None

    def get_dataset_table(self):
        with self.dm_cursor:
            dataset_id_ls, dataset_name_ls = self._select_all_records_in_dataset_table()
        return dataset_id_ls, dataset_name_ls

    def change_present_data_set(self, data_set_id):
        '''
        改变当前的dataset， 返回 data set 对应的名字
        :param data_set_id: 新的data_set_id
        :return: 如果data_set_id存在，返回对应的data set name， 否则返回 None
        '''
        with self.dm_cursor:
            # TODO: 判断data set id 是否存在
            dataset_id_ls, dataset_name_ls = self._select_all_records_in_dataset_table()
            if data_set_id in dataset_id_ls:
                self.present_data_set_id = data_set_id
                res = self._select_table(table_name='dataSetTable', name_ls=('name',), condition=f'id = {data_set_id}')
                return res[0][0]
            else:
                return None

    def delete_dataset_by_id(self, dataset_id: int):
        """

        :param dataset_id:
        :return:
        """
        with self.dm_cursor:
            self._delete_table(table_name='dataSetTable', condition=f"id = {dataset_id}")
            self.dm_cursor.commit()

    def _select_all_records_in_dataset_table(self):
        """
        :return: tuple (list of data_set_id, list of data_set_name)
        """
        res1 = []
        res2 = []
        res_ls = self._select_table(table_name='dataSetTable', name_ls=('id', 'name'))
        for data_set in res_ls:
            res1.append(data_set[0])
            res2.append(data_set[1])
        return res1, res2

    def _insert_table(self, table_name: str, value_tuple: tuple, name_ls=None):
        self.__insert_without_commit(table_name, value_tuple, name_ls)
        self.dm_cursor.commit()

    def __insert_without_commit(self, table_name: str, value_tuple: tuple, name_ls=None):
        '''

        :param table_name: 表名例如 'maxIdTable'
        :param value_tuple: 要插入的变量值 tuple
        :param name_ls: 要插入的变量名 tuple
        :return:  None
        '''
        n_values = len(value_tuple)
        value_ls = []
        if n_values == 0:
            raise ValueError("value list 长度不能为零")
        else:
            for value in value_tuple:
                if isinstance(value, str):
                    value_ls.append(f"'{value}'")
                else:
                    value_ls.append(value)
            value_str = ', '.join(f"{i}" for i in value_ls)

        if name_ls is None:
            sql_str = f"INSERT INTO {table_name} VALUES ({value_str})"
        else:
            if len(name_ls) != n_values:
                raise IndexError("the length of the insert values are not equalled with the names")

            sql_str = f"INSERT INTO {table_name} ({', '.join(i for i in name_ls)}) VALUES ({value_str}) "
        self.dm_cursor.sql_write_without_commit(sql_str)

    def _update_table(self, table_name: str, var_dict: dict, condition: str):
        '''

        :param table_name:  表名例如 'maxIdTable'
        :param var_dict:  要修改的变量 字典类型 变量名 对应 变量值 ， 例如 var_dict={'runId': self.present_run_id}
        :param condition: 条件，例如 'id = 0'
        :return: 没有return
        '''

        var_ls = []
        for t_key, t_var in var_dict.items():
            if isinstance(t_var, str):
                var_ls.append(f"{t_key} = '{t_var}'")
            else:
                var_ls.append(f"{t_key} = {t_var}")
        if len(var_ls) == 0:
            raise ValueError("要修改的变量不能为空")

        sql_str = f"UPDATE {table_name}" \
                  f" SET {', '.join(i for i in var_ls)}" \
                  f" WHERE {condition}"
        self.dm_cursor.sql_write(sql_str)

    def _delete_table(self, table_name: str, condition):
        """
        delete records from table
        :param table_name:
        :param condition:
        :return:
        """
        self.dm_cursor.sql_write(f"DELETE FROM {table_name} WHERE {condition}")

    def _select_table(self, table_name: str, name_ls: tuple, condition=None, **kwargs):
        '''

        :param table_name: 表名, 例如 table_name='maxIdTable',
        :param name_ls: 要选择的变量名 tuple, tuple 一定要以 ", "结尾，例如：  ('runSetId', 'runId'， )
        :param condition:  条件
        :return: 返回list[tuple(var1, var2, ...)], 例如： [(0, 0)]
        '''
        if len(name_ls) == 0:
            raise ValueError("value list 长度不能为零")

        if condition is None:
            sel_str = f"SELECT {', '.join(i for i in name_ls)} FROM {table_name}"
        else:
            sel_str = f"SELECT {', '.join(i for i in name_ls)} FROM {table_name} WHERE {condition}"

        for k, v in kwargs.items():
            if (k == 'sufix') and (v is not None):
                sel_str = f"{sel_str} {v}"

        return self.dm_cursor.sql_query(sel_str)

    def _set_new_database_path(self, new_path: str):
        self.dm_cursor.set_database_path(new_path)
        # print(self._connect.get_database_path())
        # print('we run 2')
        with self.dm_cursor:
            table_ls = self.dm_cursor.sql_query("select name from sqlite_master where type='table' order by name")
            table_ls = [i[0] for i in table_ls]

            # create index table
            if 'runTable' not in table_ls:
                self._create_table_if_not_exists(table_name='runTable',
                                                 columns={
                                                     'dataSet': 'INT',
                                                     'table_id': 'TEXT UNIQUE',
                                                     'time': 'TEXT',
                                                     'label': 'TEXT',
                                                     'run_name': 'TEXT',
                                                     'type': 'TEXT',
                                                     'description': 'TEXT',
                                                     'independent_value': 'TEXT',
                                                 }, key_column=1)

            if 'dataSetTable' not in table_ls:
                self._create_table_if_not_exists(table_name='dataSetTable',
                                                 columns={
                                                     'id': 'INT',
                                                     'name': 'TEXT'
                                                 }, key_column=0)
                self.dm_cursor.sql_write("INSERT INTO dataSetTable VALUES(0, 'recycle bin')")
                self.dm_cursor.sql_write("INSERT INTO dataSetTable VALUES(1, 'default data set')")

            if 'plotSettingTable' not in table_ls:
                self._create_table_if_not_exists(table_name='plotSettingTable',
                                                 columns={
                                                     'table_id': 'TEXT UNIQUE',
                                                     'axes_num': 'INT',
                                                     'x1': 'TEXT',
                                                     'x2': 'TEXT',
                                                     'x3': 'TEXT',
                                                     'x4': 'TEXT',
                                                     'x5': 'TEXT',
                                                     'x6': 'TEXT',
                                                     'x7': 'TEXT',
                                                     'x8': 'TEXT',
                                                     'x9': 'TEXT',
                                                     'y1': 'TEXT',
                                                     'y2': 'TEXT',
                                                     'y3': 'TEXT',
                                                     'y4': 'TEXT',
                                                     'y5': 'TEXT',
                                                     'y6': 'TEXT',
                                                     'y7': 'TEXT',
                                                     'y8': 'TEXT',
                                                     'y9': 'TEXT',
                                                     'z1': 'TEXT',
                                                     'z2': 'TEXT',
                                                     'z3': 'TEXT',
                                                     'z4': 'TEXT',
                                                     'z5': 'TEXT',
                                                     'z6': 'TEXT',
                                                     'z7': 'TEXT',
                                                     'z8': 'TEXT',
                                                     'z9': 'TEXT'
                                                 }, key_column=0)

            if 'maxIdTable' not in table_ls:
                self._create_table_if_not_exists(table_name='maxIdTable',
                                                 columns={
                                                     'id': 'INT',
                                                     'runSetId': 'INT',
                                                     'runId': 'INT',
                                                 }, key_column=0)
                self.dm_cursor.sql_write("INSERT INTO maxIdTable VALUES(0, 1, 0)")
                self.present_data_set_id = 1
            else:
                res = self._select_table(table_name='maxIdTable', name_ls=('runSetId', 'runId'))
                self.present_data_set_id, self.present_run_id = res[0]
                # print(repr(res))
                # self._connect.sql_query("SELECT runSetId, runId FROM maxIdTable")


class DataBaseConnector:
    def __init__(self):
        self.__database_path = None
        self.conn = None
        self.cursor = None
        self.open_times = 0
        self.lock = threading.Lock()

    def get_database_path(self):
        return self.__database_path

    def set_database_path(self, new_path):
        # self.conn = sqlite3.connect(new_path)
        # self.conn.close()
        # self.__database_path = new_path
        try:
            self.conn = sqlite3.connect(new_path)
            self.conn.close()
            self.__database_path = new_path
        except Exception as e:
            print(f'invalid path: {new_path} for {repr(e)}')

    def sql_write(self, sql_code):
        # print(sql_code)
        self.cursor.execute(sql_code)
        self.conn.commit()

    def sql_write_without_commit(self, sql_code):
        # print(sql_code)
        self.cursor.execute(sql_code)

    def sql_query(self, sql_code):
        # print(sql_code)
        self.cursor.execute(sql_code)
        self.conn.commit()
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def __enter__(self):
        self.conn = sqlite3.connect(self.__database_path)
        self.cursor = self.conn.cursor()
        # with self.lock:
        #     if self.open_times == 0:
        #         self.conn = sqlite3.connect(self.__database_path)
        #         self.cursor = self.conn.cursor()
        #         self.open_times += 1
        #     else:
        #         self.open_times += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
        # with self.lock:
        #     self.open_times -= 1
        #     if self.open_times == 0:
        #         self.cursor.close()
        #         self.conn.close()


if __name__ == '__main__':
    dm = load_or_create_database(r'D:\project\test\example.db')
