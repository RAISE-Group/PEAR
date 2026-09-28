def _add_legend_handle(self, handle, label, index=None):
    if label is not None:
        if self.mark_right and index is not None:
            if self.on_right(index):
                label = label + ' (right)'
        self.legend_handles.append(handle)
        self.legend_labels.append(label)