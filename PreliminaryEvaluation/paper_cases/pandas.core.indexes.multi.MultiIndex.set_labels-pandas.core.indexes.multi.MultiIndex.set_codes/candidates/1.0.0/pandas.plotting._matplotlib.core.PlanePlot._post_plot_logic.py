def _post_plot_logic(self, ax, data):
    x, y = (self.x, self.y)
    ax.set_ylabel(pprint_thing(y))
    ax.set_xlabel(pprint_thing(x))