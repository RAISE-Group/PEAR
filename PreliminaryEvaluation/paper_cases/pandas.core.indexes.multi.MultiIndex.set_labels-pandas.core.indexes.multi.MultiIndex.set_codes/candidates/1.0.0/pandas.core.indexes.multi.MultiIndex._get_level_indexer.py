def _get_level_indexer(self, key, level=0, indexer=None):
    level_index = self.levels[level]
    level_codes = self.codes[level]

    def convert_indexer(start, stop, step, indexer=indexer, codes=level_codes):
        r = np.arange(start, stop, step)
        if indexer is not None and len(indexer) != len(codes):
            from pandas import Series
            mapper = Series(indexer)
            indexer = codes.take(ensure_platform_int(indexer))
            result = Series(Index(indexer).isin(r).nonzero()[0])
            m = result.map(mapper)._ndarray_values
        else:
            m = np.zeros(len(codes), dtype=bool)
            m[np.in1d(codes, r, assume_unique=Index(codes).is_unique)] = True
        return m
    if isinstance(key, slice):
        try:
            if key.start is not None:
                start = level_index.get_loc(key.start)
            else:
                start = 0
            if key.stop is not None:
                stop = level_index.get_loc(key.stop)
            else:
                stop = len(level_index) - 1
            step = key.step
        except KeyError:
            start = stop = level_index.slice_indexer(key.start, key.stop, key.step, kind='loc')
            step = start.step
        if isinstance(start, slice) or isinstance(stop, slice):
            start = getattr(start, 'start', start)
            stop = getattr(stop, 'stop', stop)
            return convert_indexer(start, stop, step)
        elif level > 0 or self.lexsort_depth == 0 or step is not None:
            return convert_indexer(start, stop + 1, step)
        else:
            i = level_codes.searchsorted(start, side='left')
            j = level_codes.searchsorted(stop, side='right')
            return slice(i, j, step)
    else:
        code = self._get_loc_single_level_index(level_index, key)
        if level > 0 or self.lexsort_depth == 0:
            locs = np.array(level_codes == code, dtype=bool, copy=False)
            if not locs.any():
                raise KeyError(key)
            return locs
        i = level_codes.searchsorted(code, side='left')
        j = level_codes.searchsorted(code, side='right')
        if i == j:
            raise KeyError(key)
        return slice(i, j)