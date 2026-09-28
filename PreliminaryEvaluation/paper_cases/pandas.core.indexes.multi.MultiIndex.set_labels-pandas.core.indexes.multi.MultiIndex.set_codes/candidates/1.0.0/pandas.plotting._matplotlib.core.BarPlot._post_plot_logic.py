def _post_plot_logic(self, ax, data):
    if self.use_index:
        str_index = [pprint_thing(key) for key in data.index]
    else:
        str_index = [pprint_thing(key) for key in range(data.shape[0])]
    name = self._get_index_name()
    s_edge = self.ax_pos[0] - 0.25 + self.lim_offset
    e_edge = self.ax_pos[-1] + 0.25 + self.bar_width + self.lim_offset
    self._decorate_ticks(ax, name, str_index, s_edge, e_edge)