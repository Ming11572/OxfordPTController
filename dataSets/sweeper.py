from PySide6.QtCore import QThread, Signal

import time
from copy import deepcopy

from PlotWindow import PlotWindow
from MappingWindow import MappingWindow
from dataSets.dynamic_data_saver import DataCollector, DataSaver


class Sweeper:

    def __init__(self, func, swp_array, pause_time, plot):
        super(Sweeper, self).__init__()
        self.swp_array: list = swp_array
        self.swp_func = func
        self.swp_remain = len(swp_array)
        self.pause_time = pause_time
        self.plot = plot
        self.index = 0
        self.flag_abort_sweeper = False

    def abort_sweeper(self):
        self.flag_abort_sweeper = True

    def continue_sweeper(self):
        self.flag_abort_sweeper = False

    def move_1_step(self):
        if self.swp_remain > 0:
            self.swp_func(self.swp_array[self.index])
            self.swp_remain -= 1
            self.index += 1
            if self.pause_time > 1:
                steps, pause_time = divmod(self.pause_time, 1)
                time.sleep(pause_time)
                for i in range(int(steps)):
                    if self.flag_abort_sweeper:
                        return
                    else:
                        time.sleep(1)
            else:
                time.sleep(self.pause_time)
            return True
        else:
            return True

    def reverse_swp(self):
        self.swp_array = list(reversed(self.swp_array))
        self.index_to_zero()

    def index_to_zero(self):
        self.index = 0
        self.swp_remain = len(self.swp_array)

    def double_swp_array(self):
        swp_array = []
        for ar in self.swp_array:
            swp_array.append(ar)
            swp_array.append(ar)
        self.swp_array = swp_array
        self.index_to_zero()


class Do2dRecipe(QThread):
    signal_next_line = Signal()
    seqs_normal_stop = Signal()
    signal_recipe_abort = Signal()
    signal_remain_point_changed = Signal(int, int)
    signal_present_seq_changed = Signal(int)

    def __init__(self, plot_window: PlotWindow):
        super(Do2dRecipe, self).__init__()
        self.plot_window = plot_window
        self.description_ls = None
        self.collector = None
        self.swp_ls = None
        self.flag_abort_recipe = False
        self.data_saver = None
        self.tb_name = None
        self.i_seq = 0
        self.n_seq = 0
        self.skip_seqs = False
        self.total_remain_point = 0
        self.total_remain_seqs = 0
        self.present_seq = 0
        self.total_seq = 0

    def new_recipe(self, data_saver: DataSaver, collector: DataCollector, swp_ls: list[Sweeper],
                   description_ls: list):
        self.data_saver = data_saver
        self.collector = collector
        self.swp_ls = swp_ls
        self.n_seq = len(self.swp_ls)
        self.flag_abort_recipe = False
        self.i_seq = 0
        self.description_ls = description_ls
        self.total_seq = len(swp_ls)
        self.total_remain_point = 0
        self.tb_name = None
        for swp in swp_ls:
            self.total_remain_point += swp.swp_remain

    def run(self) -> None:
        for i in range(self.i_seq, self.n_seq):
            if self.tb_name is None:
                self.tb_name = self.data_saver.new_db_table(i)
                self.plot_window.new_line()
            self.signal_present_seq_changed.emit(self.i_seq)

            swp: Sweeper = self.swp_ls[i]
            if swp.plot:
                self.plot_window.skip_point = 1
            else:
                self.plot_window.skip_point = 0

            for step in range(swp.swp_remain):
                if self.flag_abort_recipe:
                    self.signal_recipe_abort.emit()
                    return
                if self.skip_seqs:
                    self.total_remain_point -= swp.swp_remain
                    self.signal_remain_point_changed.emit(0, self.total_remain_point)
                    self.skip_seqs = False
                    break
                swp.move_1_step()
                self.total_remain_point -= 1
                self.signal_remain_point_changed.emit(swp.swp_remain, self.total_remain_point)

                # collector data
                res = self.collector.do_collector()

                self.data_saver.append_data(collected_datas=res, index=[swp.index], tb_name=self.tb_name)

            self.i_seq += 1
            if self.i_seq < self.n_seq:
                # self.plot_window.new_line()
                self.tb_name = None
            # self.signal_next_line.emit()
        # 退出
        self.seqs_normal_stop.emit()

    def slot_skip_seqs(self):
        self.skip_seqs = True

    def abort_recipe(self):
        self.flag_abort_recipe = True
        temp_swp: Sweeper = self.swp_ls[self.i_seq]
        temp_swp.abort_sweeper()

    def continue_recipe(self):
        self.flag_abort_recipe = False
        temp_swp: Sweeper = self.swp_ls[self.i_seq]
        temp_swp.continue_sweeper()


class DoMappingRecipe(QThread):
    signal_next_line = Signal()
    seqs_normal_stop = Signal()
    signal_recipe_abort = Signal()
    signal_remain_point_changed = Signal(int, int)
    signal_present_seq_changed = Signal(int)

    def __init__(self, mapping_window: MappingWindow):
        super(DoMappingRecipe, self).__init__()
        self.mapping_window = mapping_window
        self.data_saver = None
        self.tb_bkw = None
        self.tb_frw = None
        self.collector = None
        self.loop1 = None
        self.loop2 = None
        self.index = 0
        self.i_seq = 0
        self.total_remain_point = 0
        self.n_seq = 0
        self.mapping_direction = 0
        self.mapping_type = 1
        self.flag_reverse_swp = False
        self.flag_abort_recipe = False

    def new_recipe(self, data_saver: DataSaver, collector: DataCollector, loop1, loop2, mapping_type):
        self.collector = collector
        self.loop1: Sweeper = loop1
        self.loop2: Sweeper = loop2

        self.flag_abort_recipe = False
        self.data_saver = data_saver
        self.tb_frw = None
        self.tb_bkw = None

        self.mapping_type = mapping_type
        if self.mapping_type == 2:
            self.loop1.double_swp_array()
        self.total_remain_point = self.loop1.swp_remain * self.loop2.swp_remain
        self.index = 0
        self.i_seq = 0
        self.n_seq = deepcopy(self.loop1.swp_remain)

    def run(self) -> None:
        if self.tb_frw is None:
            self.tb_frw = self.data_saver.new_db_table("forward")
            if self.mapping_type == 2:
                self.tb_bkw = self.data_saver.new_db_table("backward")

        for i in range(self.i_seq, self.n_seq):
            self.loop1.move_1_step()
            if self.flag_reverse_swp:
                self.loop2.reverse_swp()
                self.flag_reverse_swp = False
            # inside loop
            for j in range(self.loop2.swp_remain):
                if self.flag_abort_recipe:
                    self.signal_recipe_abort.emit()
                    return
                self.loop2.move_1_step()
                self.total_remain_point -= 1
                self.signal_remain_point_changed.emit(self.loop2.swp_remain, self.total_remain_point)
                self.index += 1

                # collector data
                res = self.collector.do_collector()
                index_ls = [self.index, f"loop1_{self.loop1.index}", f"loop2_{self.loop2.index}"]
                if self.mapping_direction == 0:
                    self.data_saver.append_data(res, index_ls, self.tb_frw)
                    # self.mapping_window.pumped_data(row_datas)
                elif self.mapping_direction == 1:
                    self.data_saver.append_data(res, index_ls, self.tb_bkw)
                    # self.mapping_window.pumped_data(row_datas)
            self.i_seq += 1
            # self.signal_next_line.emit()
            self.mapping_window.add_lines_to_mapping(mapping_direction=self.mapping_direction,
                                                     mapping_type=self.mapping_type)
            if self.mapping_direction == 0:
                self.mapping_direction = 1
            else:
                self.mapping_direction = 0
            self.flag_reverse_swp = True
            self.signal_present_seq_changed.emit(self.i_seq)
            self.data_saver.new_seq_t0()

        # 退出
        self.seqs_normal_stop.emit()

    def abort_recipe(self):
        self.flag_abort_recipe = True
        self.loop1.abort_sweeper()
        self.loop2.abort_sweeper()

    def continue_recipe(self):
        self.flag_abort_recipe = False
        self.loop1.continue_sweeper()
        self.loop2.continue_sweeper()




