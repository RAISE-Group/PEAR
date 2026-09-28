@pytest.mark.parametrize('series, func, expected', chain(_get_cython_table_params(Series(dtype=np.float64), [('cumprod', Series([], Index([]), dtype=np.float64)), ('cumsum', Series([], Index([]), dtype=np.float64))]), _get_cython_table_params(Series([np.nan, 1, 2, 3]), [('cumprod', Series([np.nan, 1, 2, 6])), ('cumsum', Series([np.nan, 1, 3, 6]))]), _get_cython_table_params(Series('a b c'.split()), [('cumsum', Series(['a', 'ab', 'abc']))])))
def test_agg_cython_table_transform(self, series, func, expected):
    result = series.agg(func)
    tm.assert_series_equal(result, expected)