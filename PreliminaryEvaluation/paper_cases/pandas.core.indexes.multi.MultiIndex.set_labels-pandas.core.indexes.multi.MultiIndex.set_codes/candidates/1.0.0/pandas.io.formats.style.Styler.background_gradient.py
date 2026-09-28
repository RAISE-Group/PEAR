def background_gradient(self, cmap='PuBu', low=0, high=0, axis=0, subset=None, text_color_threshold=0.408, vmin: Optional[float]=None, vmax: Optional[float]=None):
    """
        Color the background in a gradient style.

        The background color is determined according
        to the data in each column (optionally row). Requires matplotlib.

        Parameters
        ----------
        cmap : str or colormap
            Matplotlib colormap.
        low : float
            Compress the range by the low.
        high : float
            Compress the range by the high.
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            Apply to each column (``axis=0`` or ``'index'``), to each row
            (``axis=1`` or ``'columns'``), or to the entire DataFrame at once
            with ``axis=None``.
        subset : IndexSlice
            A valid slice for ``data`` to limit the style application to.
        text_color_threshold : float or int
            Luminance threshold for determining text color. Facilitates text
            visibility across varying background colors. From 0 to 1.
            0 = all text is dark colored, 1 = all text is light colored.

            .. versionadded:: 0.24.0

        vmin : float, optional
            Minimum data value that corresponds to colormap minimum value.
            When None (default): the minimum value of the data will be used.

            .. versionadded:: 1.0.0

        vmax : float, optional
            Maximum data value that corresponds to colormap maximum value.
            When None (default): the maximum value of the data will be used.

            .. versionadded:: 1.0.0

        Returns
        -------
        self : Styler

        Raises
        ------
        ValueError
            If ``text_color_threshold`` is not a value from 0 to 1.

        Notes
        -----
        Set ``text_color_threshold`` or tune ``low`` and ``high`` to keep the
        text legible by not using the entire range of the color map. The range
        of the data is extended by ``low * (x.max() - x.min())`` and ``high *
        (x.max() - x.min())`` before normalizing.
        """
    subset = _maybe_numeric_slice(self.data, subset)
    subset = _non_reducing_slice(subset)
    self.apply(self._background_gradient, cmap=cmap, subset=subset, axis=axis, low=low, high=high, text_color_threshold=text_color_threshold, vmin=vmin, vmax=vmax)
    return self