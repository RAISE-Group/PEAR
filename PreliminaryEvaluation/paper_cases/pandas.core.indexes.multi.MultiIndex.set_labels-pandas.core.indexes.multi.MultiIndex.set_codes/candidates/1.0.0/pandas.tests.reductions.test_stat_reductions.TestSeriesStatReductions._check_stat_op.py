def _check_stat_op(self, name, alternate, string_series_, check_objects=False, check_allna=False):
    with pd.option_context('use_bottleneck', False):
        f = getattr(Series, name)
        string_series_[5:15] = np.NaN
        if name not in ['max', 'min', 'mean']:
            ds = Series(pd.date_range('1/1/2001', periods=10))
            with pytest.raises(TypeError):
                f(ds)
        assert pd.notna(f(string_series_))
        assert pd.isna(f(string_series_, skipna=False))
        nona = string_series_.dropna()
        tm.assert_almost_equal(f(nona), alternate(nona.values))
        tm.assert_almost_equal(f(string_series_), alternate(nona.values))
        allna = string_series_ * np.nan
        if check_allna:
            assert np.isnan(f(allna))
        s = Series([1, 2, 3, None, 5])
        f(s)
        items = [0]
        items.extend(range(2 ** 40, 2 ** 40 + 1000))
        s = Series(items, dtype='int64')
        tm.assert_almost_equal(float(f(s)), float(alternate(s.values)))
        if check_objects:
            s = Series(pd.bdate_range('1/1/2000', periods=10))
            res = f(s)
            exp = alternate(s)
            assert res == exp
        if name not in ['sum', 'min', 'max']:
            with pytest.raises(TypeError):
                f(Series(list('abc')))
        with pytest.raises(ValueError):
            f(string_series_, axis=1)
        if 'numeric_only' in inspect.getfullargspec(f).args:
            with pytest.raises(NotImplementedError, match=name):
                f(string_series_, numeric_only=True)