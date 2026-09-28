def _get_axis_resolvers(self, axis: str) -> Dict[str, ABCSeries]:
    axis_index = getattr(self, axis)
    d = dict()
    prefix = axis[0]
    for i, name in enumerate(axis_index.names):
        if name is not None:
            key = level = name
        else:
            key = f'{prefix}level_{i}'
            level = i
        level_values = axis_index.get_level_values(level)
        s = level_values.to_series()
        s.index = axis_index
        d[key] = s
    if isinstance(axis_index, MultiIndex):
        dindex = axis_index
    else:
        dindex = axis_index.to_series()
    d[axis] = dindex
    return d