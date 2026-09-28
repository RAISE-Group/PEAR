def test_value_counts_unique_nunique(self):
    for orig in self.objs:
        o = orig.copy()
        klass = type(o)
        values = o._values
        if isinstance(values, Index):
            values.name = None
        if isinstance(o, Index) and o.is_boolean():
            continue
        elif isinstance(o, Index):
            expected_index = Index(o[::-1])
            expected_index.name = None
            o = o.repeat(range(1, len(o) + 1))
            o.name = 'a'
        else:
            expected_index = Index(values[::-1])
            idx = o.index.repeat(range(1, len(o) + 1))
            indices = np.repeat(np.arange(len(o)), range(1, len(o) + 1))
            rep = values.take(indices)
            o = klass(rep, index=idx, name='a')
        assert o.dtype == orig.dtype
        expected_s = Series(range(10, 0, -1), index=expected_index, dtype='int64', name='a')
        result = o.value_counts()
        tm.assert_series_equal(result, expected_s)
        assert result.index.name is None
        assert result.name == 'a'
        result = o.unique()
        if isinstance(o, Index):
            assert isinstance(result, type(o))
            tm.assert_index_equal(result, orig)
            assert result.dtype == orig.dtype
        elif is_datetime64tz_dtype(o):
            assert result[0] == orig[0]
            for r in result:
                assert isinstance(r, Timestamp)
            tm.assert_numpy_array_equal(result.astype(object), orig._values.astype(object))
        else:
            tm.assert_numpy_array_equal(result, orig.values)
            assert result.dtype == orig.dtype
        assert o.nunique() == len(np.unique(o.values))