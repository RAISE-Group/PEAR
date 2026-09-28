def _validate_color_args(self):
    if 'color' in self.kwds:
        if self.colormap is not None:
            warnings.warn("'color' and 'colormap' cannot be used simultaneously. Using 'color'")
        self.color = self.kwds.pop('color')
        if isinstance(self.color, dict):
            valid_keys = ['boxes', 'whiskers', 'medians', 'caps']
            for key, values in self.color.items():
                if key not in valid_keys:
                    raise ValueError(f"color dict contains invalid key '{key}'. The key must be either {valid_keys}")
    else:
        self.color = None
    colors = _get_standard_colors(num_colors=3, colormap=self.colormap, color=None)
    self._boxes_c = colors[0]
    self._whiskers_c = colors[0]
    self._medians_c = colors[2]
    self._caps_c = 'k'