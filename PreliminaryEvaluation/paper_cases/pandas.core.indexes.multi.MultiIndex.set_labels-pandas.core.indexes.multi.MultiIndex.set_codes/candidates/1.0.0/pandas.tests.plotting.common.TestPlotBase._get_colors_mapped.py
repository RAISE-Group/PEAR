def _get_colors_mapped(self, series, colors):
    unique = series.unique()
    mapped = dict(zip(unique, colors))
    return [mapped[v] for v in series.values]