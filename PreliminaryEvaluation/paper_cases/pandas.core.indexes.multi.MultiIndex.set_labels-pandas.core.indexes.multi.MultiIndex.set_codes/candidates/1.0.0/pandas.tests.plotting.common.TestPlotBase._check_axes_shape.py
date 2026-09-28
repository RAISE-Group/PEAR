def _check_axes_shape(self, axes, axes_num=None, layout=None, figsize=None):
    """
        Check expected number of axes is drawn in expected layout

        Parameters
        ----------
        axes : matplotlib Axes object, or its list-like
        axes_num : number
            expected number of axes. Unnecessary axes should be set to
            invisible.
        layout : tuple
            expected layout, (expected number of rows , columns)
        figsize : tuple
            expected figsize. default is matplotlib default
        """
    from pandas.plotting._matplotlib.tools import _flatten
    if figsize is None:
        figsize = self.default_figsize
    visible_axes = self._flatten_visible(axes)
    if axes_num is not None:
        assert len(visible_axes) == axes_num
        for ax in visible_axes:
            assert len(ax.get_children()) > 0
    if layout is not None:
        result = self._get_axes_layout(_flatten(axes))
        assert result == layout
    tm.assert_numpy_array_equal(visible_axes[0].figure.get_size_inches(), np.array(figsize, dtype=np.float64))