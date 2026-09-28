def check_ops_properties(self, props, filter=None, ignore_failures=False):
    for op in props:
        for o in self.is_valid_objs:
            if filter is not None:
                filt = o.index if isinstance(o, Series) else o
                if not filter(filt):
                    continue
            try:
                if isinstance(o, Series):
                    expected = Series(getattr(o.index, op), index=o.index, name='a')
                else:
                    expected = getattr(o, op)
            except AttributeError:
                if ignore_failures:
                    continue
            result = getattr(o, op)
            if isinstance(result, Series) and isinstance(expected, Series):
                tm.assert_series_equal(result, expected)
            elif isinstance(result, Index) and isinstance(expected, Index):
                tm.assert_index_equal(result, expected)
            elif isinstance(result, np.ndarray) and isinstance(expected, np.ndarray):
                tm.assert_numpy_array_equal(result, expected)
            else:
                assert result == expected
        if not ignore_failures:
            for o in self.not_valid_objs:
                err = AttributeError
                if issubclass(type(o), DatetimeIndexOpsMixin):
                    err = TypeError
                with pytest.raises(err):
                    getattr(o, op)