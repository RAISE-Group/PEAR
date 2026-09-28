def _get_ax_legend_handle(self, ax):
    """
        Take in axes and return ax, legend and handle under different scenarios
        """
    leg = ax.get_legend()
    handle, _ = ax.get_legend_handles_labels()
    other_ax = getattr(ax, 'left_ax', None) or getattr(ax, 'right_ax', None)
    other_leg = None
    if other_ax is not None:
        other_leg = other_ax.get_legend()
    if leg is None and other_leg is not None:
        leg = other_leg
        ax = other_ax
    return (ax, leg, handle)