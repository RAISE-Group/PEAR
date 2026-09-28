def _get_colors(self, num_colors=None, color_kwds='color'):
    if num_colors is None:
        num_colors = self.nseries
    return _get_standard_colors(num_colors=num_colors, colormap=self.colormap, color=self.kwds.get(color_kwds))