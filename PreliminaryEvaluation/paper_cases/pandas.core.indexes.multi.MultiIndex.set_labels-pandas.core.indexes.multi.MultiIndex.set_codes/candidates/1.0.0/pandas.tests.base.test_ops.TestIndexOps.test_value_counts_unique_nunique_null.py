@pytest.mark.parametrize('null_obj', [np.nan, None])
def test_value_counts_unique_nunique_null(self, null_obj):
    for orig in self.objs:
        o = orig.copy()
        klass = type(o)
        values = o._ndarray_values
        if not self._allow_na_ops(o):
            continue
        if is_datetime64tz_dtype(o):
            if isinstance(o, DatetimeIndex):
                v = o.asi8
                v[0:2] = iNaT
                values = o._shallow_copy(v)
            else:
                o = o.copy()
                o[0:2] = pd.NaT
                values = o._values
        elif needs_i8_conversion(o):
            values[0:2] = iNaT
            values = o._shallow_copy(values)
        else:
            values[0:2] = null_obj
        assert values.dtype == o.dtype
        if isinstance(o, (DatetimeIndex, PeriodIndex)):
            expected_index = o.copy()
            expected_index.name = None
            o = klass(values.repeat(range(1, len(o) + 1)))
            o.name = 'a'
        else:
            if isinstance(o, DatetimeIndex):
                expected_index = orig._values._shallow_copy(values)
            else:
                expected_index = Index(values)
            expected_index.name = None
            o = o.repeat(range(1, len(o) + 1))
            o.name = 'a'
        assert o.dtype == orig.dtype
        nanloc = np.zeros(len(o), dtype=np.bool)
        nanloc[:3] = True
        if isinstance(o, Index):
            tm.assert_numpy_array_equal(pd.isna(o), nanloc)
        else:
            exp = Series(nanloc, o.index, name='a')
            tm.assert_series_equal(pd.isna(o), exp)
        expected_s_na = Series(list(range(10, 2, -1)) + [3], index=expected_index[9:0:-1], dtype='int64', name='a')
        expected_s = Series(list(range(10, 2, -1)), index=expected_index[9:1:-1], dtype='int64', name='a')
        result_s_na = o.value_counts(dropna=False)
        tm.assert_series_equal(result_s_na, expected_s_na)
        assert result_s_na.index.name is None
        assert result_s_na.name == 'a'
        result_s = o.value_counts()
        tm.assert_series_equal(o.value_counts(), expected_s)
        assert result_s.index.name is None
        assert result_s.name == 'a'
        result = o.unique()
        if isinstance(o, Index):
            tm.assert_index_equal(result, Index(values[1:], name='a'))
        elif is_datetime64tz_dtype(o):
            tm.assert_extension_array_equal(result[1:], values[2:])
            assert result[0] is pd.NaT
        else:
            tm.assert_numpy_array_equal(result[1:], values[2:])
            assert pd.isna(result[0])
            assert result.dtype == orig.dtype
        assert o.nunique() == 8
        assert o.nunique(dropna=False) == 9