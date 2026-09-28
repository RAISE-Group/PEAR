def _make_plot(self):
    if self._is_ts_plot():
        from pandas.plotting._matplotlib.timeseries import _maybe_convert_index
        data = _maybe_convert_index(self._get_ax(0), self.data)
        x = data.index
        plotf = self._ts_plot
        it = self._iter_data(data=data, keep_index=True)
    else:
        x = self._get_xticks(convert_period=True)
        plotf = self._plot
        it = self._iter_data()
    stacking_id = self._get_stacking_id()
    is_errorbar = com.any_not_none(*self.errors.values())
    colors = self._get_colors()
    for i, (label, y) in enumerate(it):
        ax = self._get_ax(i)
        kwds = self.kwds.copy()
        style, kwds = self._apply_style_colors(colors, kwds, i, label)
        errors = self._get_errorbars(label=label, index=i)
        kwds = dict(kwds, **errors)
        label = pprint_thing(label)
        kwds['label'] = label
        newlines = plotf(ax, x, y, style=style, column_num=i, stacking_id=stacking_id, is_errorbar=is_errorbar, **kwds)
        self._add_legend_handle(newlines[0], label, index=i)
        if self._is_ts_plot():
            lines = _get_all_lines(ax)
            left, right = _get_xlim(lines)
            ax.set_xlim(left, right)