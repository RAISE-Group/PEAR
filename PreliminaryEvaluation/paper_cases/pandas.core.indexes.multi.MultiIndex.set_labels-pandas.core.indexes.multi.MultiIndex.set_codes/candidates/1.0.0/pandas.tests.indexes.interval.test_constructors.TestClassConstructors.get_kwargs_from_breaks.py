def get_kwargs_from_breaks(self, breaks, closed='right'):
    """
        converts intervals in breaks format to a dictionary of kwargs to
        specific to the format expected by the IntervalIndex/Index constructors
        """
    if len(breaks) == 0:
        return {'data': breaks}
    ivs = [Interval(l, r, closed) if notna(l) else l for l, r in zip(breaks[:-1], breaks[1:])]
    if isinstance(breaks, list):
        return {'data': ivs}
    elif is_categorical_dtype(breaks):
        return {'data': breaks._constructor(ivs)}
    return {'data': np.array(ivs, dtype=object)}