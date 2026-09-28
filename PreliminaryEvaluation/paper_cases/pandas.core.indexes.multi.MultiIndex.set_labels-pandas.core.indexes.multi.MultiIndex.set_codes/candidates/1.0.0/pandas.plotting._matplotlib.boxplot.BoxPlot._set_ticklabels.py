def _set_ticklabels(self, ax, labels):
    if self.orientation == 'vertical':
        ax.set_xticklabels(labels)
    else:
        ax.set_yticklabels(labels)