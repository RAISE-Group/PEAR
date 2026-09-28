def _get_axes_layout(self, axes):
    x_set = set()
    y_set = set()
    for ax in axes:
        points = ax.get_position().get_points()
        x_set.add(points[0][0])
        y_set.add(points[0][1])
    return (len(y_set), len(x_set))