def _post_plot_logic(self, ax, data):
    from matplotlib.ticker import FixedLocator

    def get_label(i):
        try:
            return pprint_thing(data.index[i])
        except Exception:
            return ''
    if self._need_to_set_index:
        xticks = ax.get_xticks()
        xticklabels = [get_label(x) for x in xticks]
        ax.set_xticklabels(xticklabels)
        ax.xaxis.set_major_locator(FixedLocator(xticks))
    condition = not self._use_dynamic_x() and data.index.is_all_dates and (not self.subplots) or (self.subplots and self.sharex)
    index_name = self._get_index_name()
    if condition:
        if not self._rot_set:
            self.rot = 30
        format_date_labels(ax, rot=self.rot)
    if index_name is not None and self.use_index:
        ax.set_xlabel(index_name)