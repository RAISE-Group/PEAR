def get_kwargs_from_breaks(self, breaks, closed='right'):
    """
        converts intervals in breaks format to a dictionary of kwargs to
        specific to the format expected by IntervalIndex.from_tuples
        """
    if len(breaks) == 0:
        return {'data': breaks}
    tuples = list(zip(breaks[:-1], breaks[1:]))
    if isinstance(breaks, (list, tuple)):
        return {'data': tuples}
    elif is_categorical_dtype(breaks):
        return {'data': breaks._constructor(tuples)}
    return {'data': com.asarray_tuplesafe(tuples)}