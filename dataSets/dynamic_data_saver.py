import threading
from time import time

from PySide6.QtCore import QThread, Signal
from dataSets.data_sets import DatabaseManager
from PlotWindow import PlotWindow
from MappingWindow import MappingWindow
import math


class DataCollector:

    def __init__(self, recipe_lock: threading.Lock):
        self.recipe_lock = recipe_lock
        self.func_ls1 = None
        self.func_ls2 = None

    def set_func_ls(self, instr_ls):
        self.func_ls1 = []
        self.func_ls2 = []
        for instr in instr_ls:
            self.func_ls1.append(instr.parallel_read_part1)
            self.func_ls2.append(instr.parallel_read_part2)

    def do_collector(self):
        with self.recipe_lock:
            for temp_fun in self.func_ls1:
                temp_fun()
            res = []
            for temp_fun in self.func_ls2:
                res = res + temp_fun()
        return res


class DataSaver(QThread):
    signal_2d_data_pumped = Signal(list)
    signal_mapping_data_pumped = Signal(list)
    signal_plotter_draw = Signal(bool, list, list)

    def __init__(self, dm):
        super(DataSaver, self).__init__()
        self.recipe_t0 = None
        self.seq_t0 = None
        self.dict_var = None
        self.n_custom_var = None
        self.custom_exp_ls = None
        self.dict_custom = None
        self.dict_collect = None
        self.custom_name_ls = None
        self.collect_name_ls = None
        self.description_ls = None
        self.recipe_type = None
        self.independent_vars_ls = None
        self.var_name_ls = None
        self.index_ls = None
        self.sample_name = None
        self.data_set_id = None
        self.i_seq = None
        self.data_dict = {}
        self.table_name = None
        self.recipe_table_ls = []
        self.recipe_running = False
        self.recipe_have_run_seqs = None
        self.plotter_window = None
        self.recipe_total_datas = None
        self.mapping_total_data1 = None
        self.mapping_total_data2 = None
        self.plot_pause_time = 1

        self.signal_data_pumped = self.signal_2d_data_pumped
        self.dict_func = {'cos': self.cosd, 'sin': self.sind, 'tan': self.tand,
                          'log': self.loge, 'log10': self.log10, 'exp': math.exp}
        self.dm = dm
        self.data_lock = threading.Lock()

    def set_plot_pause_time(self, new_time: int):
        if new_time > 0:
            self.plot_pause_time = new_time

    def set_database(self, new_dm: DatabaseManager):
        self.dm = new_dm

    def new_recipe(self, sample_name, data_set_id, index_ls, collect_name_ls,
                   custom_ls, recipe_type, independent_vars_ls, description_ls, plotter_window):
        self.sample_name = sample_name
        self.data_set_id = data_set_id
        self.index_ls = index_ls

        self.custom_name_ls = []
        self.custom_exp_ls = []
        for temp in custom_ls:
            self.custom_name_ls.append(temp[0])
            self.custom_exp_ls.append(temp[1])
        self.n_custom_var = len(self.custom_name_ls)

        self.recipe_type = recipe_type
        if recipe_type == '2d':
            self.signal_data_pumped = self.signal_2d_data_pumped
            n_seqs = len(description_ls)
            self.recipe_total_datas = [[] for i in range(n_seqs)]
        else:
            self.signal_data_pumped = self.signal_mapping_data_pumped
            self.mapping_total_data1 = []
            self.mapping_total_data2 = []

        self.dict_custom = {}
        for name in self.custom_name_ls:
            self.dict_custom[name] = None

        self.var_name_ls = tuple(self.custom_name_ls + collect_name_ls)
        self.custom_name_ls = tuple(self.custom_name_ls)
        # print(self.custom_name_ls)
        # print(self.custom_exp_ls)
        if collect_name_ls is not None:
            self.dict_collect = {}
            self.collect_name_ls = tuple(collect_name_ls)
            for collected_name in collect_name_ls:
                self.dict_collect[collected_name] = None
        else:
            self.collect_name_ls = ()

        self.dict_var = {}
        for name in self.var_name_ls:
            self.dict_var[name] = None

        self.independent_vars_ls = independent_vars_ls
        self.description_ls = description_ls
        self.recipe_have_run_seqs = []
        self.recipe_t0 = time()
        self.plotter_window = plotter_window
        self.recipe_table_ls = []

    def new_db_table(self, i_seq):
        if i_seq in self.recipe_have_run_seqs:
            return None
        else:
            self.recipe_have_run_seqs.append(i_seq)
        seq_str = f"Seq{i_seq}"
        # if isinstance(i_seq, float):
        #     seq_str = f"Seq{i_seq}"
        # else:
        #     seq_str = i_seq

        self.table_name = self.dm.create_value_table(index_ls=self.index_ls,
                                                     var_name_ls=self.var_name_ls,
                                                     plot_legend=seq_str,
                                                     run_name=f"{seq_str}_{self.sample_name}",
                                                     recipe_type=self.recipe_type,
                                                     description=self.description_ls[i_seq],
                                                     independent_vars=self.independent_vars_ls[i_seq],
                                                     dataset_id=self.data_set_id)
        self.recipe_table_ls.append(self.table_name)
        self.new_seq_t0()
        return self.table_name

    def save_plot_setting_to_dm(self, axes_setting):
        self.dm.append_rows_to_plot_table(self.recipe_table_ls, axes_setting)

    def new_seq_t0(self):
        self.seq_t0 = time()

    def new_recipe_t0(self):
        self.recipe_t0 = time()

    def append_data(self, collected_datas: list, index_ls: list, i_seq, tb_name):
        present_time = time()
        time_ls = [present_time - self.recipe_t0, present_time - self.seq_t0]
        with self.data_lock:
            if tb_name in self.data_dict.keys():
                self.data_dict[tb_name].append((time_ls, collected_datas, index_ls, i_seq))
            else:
                self.data_dict[tb_name] = [(time_ls, collected_datas, index_ls, i_seq)]
        # return datas

    def run(self) -> None:
        temp_dm = DatabaseManager(self.dm.db_path)

        with temp_dm.dm_cursor:
            counts = self.plot_pause_time
            while True:
                with self.data_lock:
                    temp_dict = self.data_dict
                    self.data_dict = {}

                # 计算custom datas ,写到数据库并画图
                for k, v in temp_dict.items():
                    temp_datas_ls = []
                    for data_tuple in v:
                        time_ls, collected_datas, index_ls, i_seq = data_tuple
                        plot_datas = self.get_plotter_datas(time_ls, collected_datas)
                        self.plotter_window.pump_data(plot_datas)
                        # draw datas
                        self.recipe_total_datas[i_seq].append(plot_datas)
                        temp_datas_ls.append(tuple(index_ls + plot_datas))

                    temp_dm.append_rows_to_value_table(k, temp_datas_ls)

                    # # 清空已经保存的数据
                    # self.data_dict = {}

                if counts < 1:
                    self.signal_plotter_draw.emit(False, [], [])
                    counts = self.plot_pause_time

                if not self.recipe_running:
                    return

                self.msleep(1000)
                counts -= 1

    def check_custom_function(self, collected_datas, collect_name_ls, custom_name_ls, custom_exp_ls):
        i = 0
        dict_var = {}
        for data in collected_datas:
            dict_var[collect_name_ls[i]] = data
            i += 1
        # check custom var
        i = 0
        _flag = True
        err_str_ls = []
        for custom_name in custom_name_ls:
            try:
                dict_var[custom_name] = eval(custom_exp_ls[i], self.dict_func, dict_var)
            except Exception as e:
                _flag = False
                err_str_ls.append(repr(e))
            i += 1
        return _flag, err_str_ls

    # 计算custom data
    def get_plotter_datas(self, time_ls: list, collected_datas: list):
        count = 0
        # define collect values
        for data in collected_datas:
            self.dict_var[self.collect_name_ls[count]] = data
            count += 1
        # calculate custom values
        custom_datas = []
        for i in range(self.n_custom_var):
            self.dict_var[self.custom_name_ls[i]] = \
                eval(self.custom_exp_ls[i], self.dict_func, self.dict_var)
            custom_datas.append(self.dict_var[self.custom_name_ls[i]])

        return time_ls + custom_datas + collected_datas

    def recipe_stop(self):
        self.recipe_running = False

    def recipe_start(self):
        self.recipe_running = True

    def loge(self, a):
        if a > 0:
            return math.log(a)
        elif a < 0:
            return math.log(abs(a))
        else:
            return -30

    def log10(self, a):
        if a > 0:
            return math.log10(a)
        elif a < 0:
            return math.log10(abs(a))
        else:
            return -30

    def cosd(self, a):
        return math.cos(math.radians(a))

    def sind(self, a):
        return math.sin(math.radians(a))

    def tand(self, a):
        return math.tan(math.radians(a))


class MappingDataSaver(DataSaver):

    def __init__(self, dm):
        super().__init__(dm)
        self.plot_pause_time = 5

    def new_db_table(self, i_seq):
        if i_seq in self.recipe_have_run_seqs:
            return None
        else:
            self.recipe_have_run_seqs.append(i_seq)
        if i_seq == 0:
            seq_str = 'frw'
        else:
            seq_str = 'bkw'

        self.table_name = self.dm.create_value_table(index_ls=self.index_ls,
                                                     var_name_ls=self.var_name_ls,
                                                     plot_legend=seq_str,
                                                     run_name=f"{seq_str}_{self.sample_name}",
                                                     recipe_type=self.recipe_type,
                                                     description=self.description_ls[i_seq],
                                                     independent_vars=self.independent_vars_ls[i_seq],
                                                     dataset_id=self.data_set_id)
        self.recipe_table_ls.append(self.table_name)
        self.new_seq_t0()
        return self.table_name

    def run(self) -> None:
        temp_dm = DatabaseManager(self.dm.db_path)

        with temp_dm.dm_cursor:
            counts = self.plot_pause_time
            while True:

                with self.data_lock:
                    temp_dict = self.data_dict
                    self.data_dict = {}

                # 计算custom datas ,写到数据库并画图
                for tb_name, v in temp_dict.items():
                    temp_datas_ls = []
                    for data_tuple in v:
                        time_ls, collected_datas, index_ls, direction_id = data_tuple
                        plot_datas = self.get_plotter_datas(time_ls, collected_datas)

                        self.plotter_window.pump_data(plot_datas, direction_id)

                        temp_datas_ls.append(tuple(index_ls + plot_datas))

                    temp_dm.append_rows_to_value_table(tb_name, temp_datas_ls)

                if counts < 1:
                    self.signal_plotter_draw.emit(False, [], [])
                    # print('start mapping')
                    counts = self.plot_pause_time

                if not self.recipe_running:
                    return

                self.msleep(1000)
                counts -= 1




