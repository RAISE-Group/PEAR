def _post_plot_logic(self, ax, data):
    if self.orientation == 'horizontal':
        ax.set_xlabel('Frequency')
    else:
        ax.set_ylabel('Frequency')