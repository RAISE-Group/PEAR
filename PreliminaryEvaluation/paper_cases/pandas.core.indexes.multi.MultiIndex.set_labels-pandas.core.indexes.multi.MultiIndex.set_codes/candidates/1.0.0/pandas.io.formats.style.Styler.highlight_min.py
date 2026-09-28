def highlight_min(self, subset=None, color='yellow', axis=0):
    """
        Highlight the minimum by shading the background.

        Parameters
        ----------
        subset : IndexSlice, default None
            A valid slice for ``data`` to limit the style application to.
        color : str, default 'yellow'
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            Apply to each column (``axis=0`` or ``'index'``), to each row
            (``axis=1`` or ``'columns'``), or to the entire DataFrame at once
            with ``axis=None``.

        Returns
        -------
        self : Styler
        """
    return self._highlight_handler(subset=subset, color=color, axis=axis, max_=False)