def test_fillna(self):
    for orig in self.objs:
        o = orig.copy()
        values = o.values
        result = o.fillna(o.astype(object).values[0])
        if isinstance(o, Index):
            tm.assert_index_equal(o, result)
        else:
            tm.assert_series_equal(o, result)
        assert o is not result
    for null_obj in [np.nan, None]:
        for orig in self.objs:
            o = orig.copy()
            klass = type(o)
            if not self._allow_na_ops(o):
                continue
            if needs_i8_conversion(o):
                values = o.astype(object).values
                fill_value = values[0]
                values[0:2] = pd.NaT
            else:
                values = o.values.copy()
                fill_value = o.values[0]
                values[0:2] = null_obj
            expected = [fill_value] * 2 + list(values[2:])
            expected = klass(expected, dtype=orig.dtype)
            o = klass(values)
            assert o.dtype == orig.dtype
            result = o.fillna(fill_value)
            if isinstance(o, Index):
                tm.assert_index_equal(result, expected)
            else:
                tm.assert_series_equal(result, expected)
            assert o is not result