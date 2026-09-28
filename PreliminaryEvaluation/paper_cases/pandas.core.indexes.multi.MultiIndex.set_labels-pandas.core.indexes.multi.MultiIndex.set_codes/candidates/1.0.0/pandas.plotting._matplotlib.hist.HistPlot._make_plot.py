def _make_plot(self):
    colors = self._get_colors()
    stacking_id = self._get_stacking_id()
    for i, (label, y) in enumerate(self._iter_data()):
        ax = self._get_ax(i)
        kwds = self.kwds.copy()
        label = pprint_thing(label)
        kwds['label'] = label
        style, kwds = self._apply_style_colors(colors, kwds, i, label)
        if style is not None:
            kwds['style'] = style
        kwds = self._make_plot_keywords(kwds, y)
        artists = self._plot(ax, y, column_num=i, stacking_id=stacking_id, **kwds)
        self._add_legend_handle(artists[0], label, index=i)