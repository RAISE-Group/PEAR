def _concat_same_dtype(self, indexes, name):
    """
        Concatenates multiple RangeIndex instances. All members of "indexes" must
        be of type RangeIndex; result will be RangeIndex if possible, Int64Index
        otherwise. E.g.:
        indexes = [RangeIndex(3), RangeIndex(3, 6)] -> RangeIndex(6)
        indexes = [RangeIndex(3), RangeIndex(4, 6)] -> Int64Index([0,1,2,4,5])
        """
    start = step = next_ = None
    non_empty_indexes = [obj for obj in indexes if len(obj)]
    for obj in non_empty_indexes:
        rng: range = obj._range
        if start is None:
            start = rng.start
            if step is None and len(rng) > 1:
                step = rng.step
        elif step is None:
            if rng.start == start:
                result = Int64Index(np.concatenate([x._values for x in indexes]))
                return result.rename(name)
            step = rng.start - start
        non_consecutive = step != rng.step and len(rng) > 1 or (next_ is not None and rng.start != next_)
        if non_consecutive:
            result = Int64Index(np.concatenate([x._values for x in indexes]))
            return result.rename(name)
        if step is not None:
            next_ = rng[-1] + step
    if non_empty_indexes:
        stop = non_empty_indexes[-1].stop if next_ is None else next_
        return RangeIndex(start, stop, step).rename(name)
    return RangeIndex(0, 0).rename(name)