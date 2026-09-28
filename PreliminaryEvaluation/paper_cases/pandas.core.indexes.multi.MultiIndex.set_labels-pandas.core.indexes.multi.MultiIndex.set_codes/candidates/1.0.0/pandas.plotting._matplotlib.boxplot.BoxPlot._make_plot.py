def _make_plot(self):
    if self.subplots:
        self._return_obj = pd.Series(dtype=object)
        for i, (label, y) in enumerate(self._iter_data()):
            ax = self._get_ax(i)
            kwds = self.kwds.copy()
            ret, bp = self._plot(ax, y, column_num=i, return_type=self.return_type, **kwds)
            self.maybe_color_bp(bp)
            self._return_obj[label] = ret
            label = [pprint_thing(label)]
            self._set_ticklabels(ax, label)
    else:
        y = self.data.values.T
        ax = self._get_ax(0)
        kwds = self.kwds.copy()
        ret, bp = self._plot(ax, y, column_num=0, return_type=self.return_type, **kwds)
        self.maybe_color_bp(bp)
        self._return_obj = ret
        labels = [l for l, _ in self._iter_data()]
        labels = [pprint_thing(l) for l in labels]
        if not self.use_index:
            labels = [pprint_thing(key) for key in range(len(labels))]
        self._set_ticklabels(ax, labels)