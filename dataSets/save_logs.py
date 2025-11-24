from dataSets.data_sets import DatabaseManager

from PySide6.QtCore import QThread, Signal
from threading import Lock

import os
from datetime import datetime


trans_table = str.maketrans(""""'""", '..')


def delete_quota_mark(text: str):
    return text.translate(trans_table)


class LogSaver(DatabaseManager, QThread):
    signal_warm_msg = Signal(int, str, str)

    def __init__(self, logging_path):
        full_path = os.path.join(logging_path, f"{datetime.now().strftime('%Y-%m')}.db")
        DatabaseManager.__init__(self, full_path)
        QThread.__init__(self, parent=None)
        self.log_dict = {}
        self.data_lock = Lock()
        self.program_quit = False
        self.gpib_logging_id = 0

    def _set_new_database_path(self, new_path: str):
        self.dm_cursor.set_database_path(new_path)
        # print('we run 1')
        with self.dm_cursor:
            table_ls = self.dm_cursor.sql_query("select name from sqlite_master where type='table' order by name")
            table_ls = [i[0] for i in table_ls]
            # print(table_ls)
            if 'teslatronPT_logging' not in table_ls:
                self._create_table_with_auto_increment_key(table_name='teslatronPT_logging',
                                                           columns={
                                                               'time': 'DOUBLE',
                                                               'probe_temp': 'DOUBLE',
                                                               'magnet': 'DOUBLE',
                                                               'vti_temp': 'DOUBLE',
                                                               'magnet_temp': 'DOUBLE',
                                                               'probe_heater_power': 'DOUBLE',
                                                               'vti_heater_power': 'DOUBLE',
                                                               'nv': 'DOUBLE',
                                                               'pressure': 'DOUBLE',
                                                               'pt1_temp': 'DOUBLE',
                                                               "pt2_temp": "DOUBLE",
                                                           })

            if 'gpib_logging' not in table_ls:
                self._create_table_with_auto_increment_key(table_name='gpib_logging',
                                                           columns={
                                                               'time': 'TEXT',
                                                               'instr_alias': 'TEXT',
                                                               'input_code': 'TEXT',
                                                               'error_msg': 'TEXT'
                                                           })
            self.__write_15000_rows_into_gpib_logging()

            if 'debug_logging' not in table_ls:
                self._create_table_with_auto_increment_key(table_name='debug_logging',
                                                           columns={
                                                               'time': 'TEXT',
                                                               'object': 'TEXT',
                                                               'info': 'TEXT'
                                                           })

            if 'logging_id' not in table_ls:
                self._create_table_if_not_exists(table_name='logging_id',
                                                 columns={'name': 'TEXT', 'present_id': 'INT'},
                                                 key_column=0)
                self.dm_cursor.sql_write("INSERT INTO logging_id VALUES('gpib_logging', 1)")
                self.gpib_logging_id = 1
            else:
                res = self._select_table(table_name='logging_id', name_ls=('present_id',),
                                         condition=f"name = 'gpib_logging'")
                self.gpib_logging_id = res[0][0]
            # print(self.gpib_logging_id)

    def __write_15000_rows_into_gpib_logging(self):
        """
        先获取当前行数，如果行数小于10000， 则写入至10000行
        :return:
        """
        res = self._select_table(table_name='sqlite_sequence', name_ls=('seq',),
                                 condition=f"name = 'gpib_logging'")
        if len(res) > 0:
            max_seqs = res[0][0]
            # print(max_seqs)
        else:
            max_seqs = 0
        for i in range(max_seqs + 1, 15001):
            sql_str = f"INSERT INTO gpib_logging (time, instr_alias, input_code, error_msg) " \
                      f"VALUES ('{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}', " \
                      f"'alias', 'codes', 'errors');"
            self.dm_cursor.sql_write_without_commit(sql_str)

    def _create_table_with_auto_increment_key(self, table_name: str, columns: dict):
        column_code = ["id integer primary key autoincrement"]
        i = 0
        for key, var in columns.items():
            temp_column = f"{key} {var}"

            column_code.append(temp_column)
            i += 1

        column_code = ', '.join(i for i in column_code)

        sql_code = f'CREATE TABLE IF NOT EXISTS {table_name} ( {column_code} )'

        self.dm_cursor.sql_write(sql_code)

    def append_log(self, log_table, log_row):
        with self.data_lock:
            if log_table in self.log_dict.keys():
                self.log_dict[log_table].append(log_row)
            else:
                self.log_dict[log_table] = [log_row]

    def log_debug(self, alias, info):
        self.append_log('debug_logging', [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), alias, info])

    def warning(self, alias, info):
        self.append_log('debug_logging', [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), alias, info])
        self.signal_warm_msg.emit(1, alias, info)

    def error(self, alias, info):
        self.append_log('debug_logging', [datetime.now().strftime('%Y/%m/%d %H:%M:%S'), alias, info])
        self.signal_warm_msg.emit(2, alias, info)

    def _write_pt_log_into_db(self, log_row: list):
        var_str = ', '.join([str(i) for i in log_row])
        sql_str = f"INSERT INTO teslatronPT_logging (time, probe_temp, magnet, vti_temp, magnet_temp, " \
                  f"probe_heater_power, vti_heater_power, nv, pressure, pt1_temp, pt2_temp) " \
                  f"VALUES ({var_str});"

        # sql_str = f"INSERT INTO teslatronPT_logging (time, probe_temperature, magnet, vti_temperature, " \
        #           f"magnet_temperature, probe_heater_power, vti_heater_power, nv, pressure) " \
        #           f"VALUES ({log_row[0]}, {log_row[1]}, {log_row[2]}, {log_row[3]}, {log_row[4]}, {log_row[5]}" \
        #           f", {log_row[6]}, {log_row[7]}, {log_row[8]});"
        self.dm_cursor.sql_write_without_commit(sql_str)

    def _write_debug_log_into_db(self, log_row: list):
        f_time, obj, info = log_row
        sql_str = f"INSERT INTO debug_logging (time, object, info) " \
                  f"VALUES ('{log_row[0]}', '{delete_quota_mark(obj)}', '{delete_quota_mark(info)}')"
        self.dm_cursor.sql_write_without_commit(sql_str)

    def _write_gpib_log_into_db(self, log_row: list):
        time, alias, i_code, err_msg = log_row

        sql_str = f"UPDATE gpib_logging " \
                  f"SET time = '{log_row[0]}', " \
                  f"instr_alias = '{delete_quota_mark(alias)}', " \
                  f"input_code = '{delete_quota_mark(i_code)}', " \
                  f"error_msg = '{delete_quota_mark(err_msg)}' " \
                  f"WHERE id = {self.gpib_logging_id}"
        self.dm_cursor.sql_write_without_commit(sql_str)

        if self.gpib_logging_id < 15000:
            self.gpib_logging_id += 1
        else:
            self.gpib_logging_id = 1

        sql_str = f"UPDATE logging_id SET present_id = {self.gpib_logging_id} WHERE name = 'gpib_logging'"
        self.dm_cursor.sql_write_without_commit(sql_str)

        # sql_str = f"UPDATE gpib_logging (time, instr_alias, input_code, error_msg) " \
        #           f"VALUES ('{log_row[0]}', '{log_row[1]}', '{log_row[2]}', '{log_row[3]}');"

    def run(self) -> None:
        with self.dm_cursor:
            while True:
                with self.data_lock:
                    temp_dict = self.log_dict
                    self.log_dict = {}

                # write log into db
                for tb_name, log_ls in temp_dict.items():
                    if tb_name == 'teslatronPT_logging':
                        temp_fun = self._write_pt_log_into_db
                    elif tb_name == 'gpib_logging':
                        temp_fun = self._write_gpib_log_into_db
                    elif tb_name == 'debug_logging':
                        temp_fun = self._write_debug_log_into_db
                    else:
                        continue
                    for log_row in log_ls:
                        temp_fun(log_row)
                    self.dm_cursor.commit()
                self.msleep(2000)
                if self.program_quit:
                    break
