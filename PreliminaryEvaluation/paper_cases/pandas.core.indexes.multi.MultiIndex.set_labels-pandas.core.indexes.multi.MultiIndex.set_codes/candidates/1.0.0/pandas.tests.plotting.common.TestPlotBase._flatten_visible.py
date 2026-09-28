def _flatten_visible(self, axes):
    """
        Flatten axes, and filter only visible

        Parameters
        ----------
        axes : matplotlib Axes object, or its list-like

        """
    from pandas.plotting._matplotlib.tools import _flatten
    axes = _flatten(axes)
    axes = [ax for ax in axes if ax.get_visible()]
    return axes