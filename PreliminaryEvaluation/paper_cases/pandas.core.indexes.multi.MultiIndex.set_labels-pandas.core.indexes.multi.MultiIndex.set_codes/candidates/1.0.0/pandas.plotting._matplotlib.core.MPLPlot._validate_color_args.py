def _validate_color_args(self):
    import matplotlib.colors
    if 'color' in self.kwds and self.nseries == 1 and (not is_list_like(self.kwds['color'])):
        self.kwds['color'] = [self.kwds['color']]
    if 'color' in self.kwds and isinstance(self.kwds['color'], tuple) and (self.nseries == 1) and (len(self.kwds['color']) in (3, 4)):
        self.kwds['color'] = [self.kwds['color']]
    if ('color' in self.kwds or 'colors' in self.kwds) and self.colormap is not None:
        warnings.warn("'color' and 'colormap' cannot be used simultaneously. Using 'color'")
    if 'color' in self.kwds and self.style is not None:
        if is_list_like(self.style):
            styles = self.style
        else:
            styles = [self.style]
        for s in styles:
            for char in s:
                if char in matplotlib.colors.BASE_COLORS:
                    raise ValueError("Cannot pass 'style' string with a color symbol and 'color' keyword argument. Please use one or the other or pass 'style' without a color symbol")