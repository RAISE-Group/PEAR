def _make_plot(self):
    colors = self._get_colors(num_colors=len(self.data), color_kwds='colors')
    self.kwds.setdefault('colors', colors)
    for i, (label, y) in enumerate(self._iter_data()):
        ax = self._get_ax(i)
        if label is not None:
            label = pprint_thing(label)
            ax.set_ylabel(label)
        kwds = self.kwds.copy()

        def blank_labeler(label, value):
            if value == 0:
                return ''
            else:
                return label
        idx = [pprint_thing(v) for v in self.data.index]
        labels = kwds.pop('labels', idx)
        if labels is not None:
            blabels = [blank_labeler(l, value) for l, value in zip(labels, y)]
        else:
            blabels = None
        results = ax.pie(y, labels=blabels, **kwds)
        if kwds.get('autopct', None) is not None:
            patches, texts, autotexts = results
        else:
            patches, texts = results
            autotexts = []
        if self.fontsize is not None:
            for t in texts + autotexts:
                t.set_fontsize(self.fontsize)
        leglabels = labels if labels is not None else idx
        for p, l in zip(patches, leglabels):
            self._add_legend_handle(p, l)