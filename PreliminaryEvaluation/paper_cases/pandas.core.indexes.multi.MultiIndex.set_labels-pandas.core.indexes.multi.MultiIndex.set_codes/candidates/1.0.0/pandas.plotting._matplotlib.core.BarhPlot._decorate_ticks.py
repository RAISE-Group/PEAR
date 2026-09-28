def _decorate_ticks(self, ax, name, ticklabels, start_edge, end_edge):
    ax.set_ylim((start_edge, end_edge))
    ax.set_yticks(self.tick_pos)
    ax.set_yticklabels(ticklabels)
    if name is not None and self.use_index:
        ax.set_ylabel(name)