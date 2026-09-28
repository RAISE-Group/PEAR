def _maybe_right_yaxis(self, ax, axes_num):
    if not self.on_right(axes_num):
        return self._get_ax_layer(ax)
    if hasattr(ax, 'right_ax'):
        return ax.right_ax
    elif hasattr(ax, 'left_ax'):
        return ax
    else:
        orig_ax, new_ax = (ax, ax.twinx())
        new_ax._get_lines = orig_ax._get_lines
        new_ax._get_patches_for_fill = orig_ax._get_patches_for_fill
        orig_ax.right_ax, new_ax.left_ax = (new_ax, orig_ax)
        if not self._has_plotted_object(orig_ax):
            orig_ax.get_yaxis().set_visible(False)
        if self.logy is True or self.loglog is True:
            new_ax.set_yscale('log')
        elif self.logy == 'sym' or self.loglog == 'sym':
            new_ax.set_yscale('symlog')
        return new_ax