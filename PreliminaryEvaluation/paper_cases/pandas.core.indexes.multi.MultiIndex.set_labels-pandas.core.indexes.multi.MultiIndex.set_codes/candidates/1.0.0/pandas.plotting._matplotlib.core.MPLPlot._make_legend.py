def _make_legend(self):
    ax, leg, handle = self._get_ax_legend_handle(self.axes[0])
    handles = []
    labels = []
    title = ''
    if not self.subplots:
        if leg is not None:
            title = leg.get_title().get_text()
            handles.extend(handle)
            labels = [x.get_text() for x in leg.get_texts()]
        if self.legend:
            if self.legend == 'reverse':
                self.legend_handles = reversed(self.legend_handles)
                self.legend_labels = reversed(self.legend_labels)
            handles += self.legend_handles
            labels += self.legend_labels
            if self.legend_title is not None:
                title = self.legend_title
        if len(handles) > 0:
            ax.legend(handles, labels, loc='best', title=title)
    elif self.subplots and self.legend:
        for ax in self.axes:
            if ax.get_visible():
                ax.legend(loc='best')