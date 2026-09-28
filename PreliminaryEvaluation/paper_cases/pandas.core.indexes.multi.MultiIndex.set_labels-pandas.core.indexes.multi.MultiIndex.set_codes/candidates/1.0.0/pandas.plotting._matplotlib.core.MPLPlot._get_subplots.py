def _get_subplots(self):
    from matplotlib.axes import Subplot
    return [ax for ax in self.axes[0].get_figure().get_axes() if isinstance(ax, Subplot)]