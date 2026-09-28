def _get_ax(self, i):
    if self.subplots:
        ax = self.axes[i]
        ax = self._maybe_right_yaxis(ax, i)
        self.axes[i] = ax
    else:
        ax = self.axes[0]
        ax = self._maybe_right_yaxis(ax, i)
    ax.get_yaxis().set_visible(True)
    return ax