@pytest.mark.parametrize('df, func, expected', _get_cython_table_params(DataFrame([['a', 'b'], ['b', 'a']]), [['cumprod', TypeError]]))
def test_agg_cython_table_raises(self, df, func, expected, axis):
    with pytest.raises(expected):
        df.agg(func, axis=axis)