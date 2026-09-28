def _post_plot_logic(self, ax, data):
    LinePlot._post_plot_logic(self, ax, data)
    if self.ylim is None:
        if (data >= 0).all().all():
            ax.set_ylim(0, None)
        elif (data <= 0).all().all():
            ax.set_ylim(None, 0)