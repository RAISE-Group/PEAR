def plot(self, left, right, labels=None, vertical: bool=True):
    """
        Plot left / right DataFrames in specified layout.

        Parameters
        ----------
        left : list of DataFrames before operation is applied
        right : DataFrame of operation result
        labels : list of str to be drawn as titles of left DataFrames
        vertical : bool, default True
            If True, use vertical layout. If False, use horizontal layout.
        """
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    if not isinstance(left, list):
        left = [left]
    left = [self._conv(l) for l in left]
    right = self._conv(right)
    hcells, vcells = self._get_cells(left, right, vertical)
    if vertical:
        figsize = (self.cell_width * hcells, self.cell_height * vcells)
    else:
        figsize = (self.cell_width * hcells, self.cell_height * vcells)
    fig = plt.figure(figsize=figsize)
    if vertical:
        gs = gridspec.GridSpec(len(left), hcells)
        max_left_cols = max((self._shape(l)[1] for l in left))
        max_left_rows = max((self._shape(l)[0] for l in left))
        for i, (l, label) in enumerate(zip(left, labels)):
            ax = fig.add_subplot(gs[i, 0:max_left_cols])
            self._make_table(ax, l, title=label, height=1.0 / max_left_rows)
        ax = plt.subplot(gs[:, max_left_cols:])
        self._make_table(ax, right, title='Result', height=1.05 / vcells)
        fig.subplots_adjust(top=0.9, bottom=0.05, left=0.05, right=0.95)
    else:
        max_rows = max((self._shape(df)[0] for df in left + [right]))
        height = 1.0 / np.max(max_rows)
        gs = gridspec.GridSpec(1, hcells)
        i = 0
        for l, label in zip(left, labels):
            sp = self._shape(l)
            ax = fig.add_subplot(gs[0, i:i + sp[1]])
            self._make_table(ax, l, title=label, height=height)
            i += sp[1]
        ax = plt.subplot(gs[0, i:])
        self._make_table(ax, right, title='Result', height=height)
        fig.subplots_adjust(top=0.85, bottom=0.05, left=0.05, right=0.95)
    return fig