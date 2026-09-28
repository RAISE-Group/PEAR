@pytest.mark.parametrize('series, func, expected', chain(_get_cython_table_params(Series(dtype=np.float64), [('sum', 0), ('max', np.nan), ('min', np.nan), ('all', True), ('any', False), ('mean', np.nan), ('prod', 1), ('std', np.nan), ('var', np.nan), ('median', np.nan)]), _get_cython_table_params(Series([np.nan, 1, 2, 3]), [('sum', 6), ('max', 3), ('min', 1), ('all', True), ('any', True), ('mean', 2), ('prod', 6), ('std', 1), ('var', 1), ('median', 2)]), _get_cython_table_params(Series('a b c'.split()), [('sum', 'abc'), ('max', 'c'), ('min', 'a'), ('all', 'c'), ('any', 'a')])))
def test_agg_cython_table(self, series, func, expected):
    result = series.agg(func)
    if tm.is_number(expected):
        assert np.isclose(result, expected, equal_nan=True)
    else:
        assert result == expected