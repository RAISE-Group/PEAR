@pytest.mark.parametrize('series, func, expected', chain(_get_cython_table_params(Series('a b c'.split()), [('mean', TypeError), ('prod', TypeError), ('std', TypeError), ('var', TypeError), ('median', TypeError), ('cumprod', TypeError)])))
def test_agg_cython_table_raises(self, series, func, expected):
    with pytest.raises(expected):
        series.agg(func)