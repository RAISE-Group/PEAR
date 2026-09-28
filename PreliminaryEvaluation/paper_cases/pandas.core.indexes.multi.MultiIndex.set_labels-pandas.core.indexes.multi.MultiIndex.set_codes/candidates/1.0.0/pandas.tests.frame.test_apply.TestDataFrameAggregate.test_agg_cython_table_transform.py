@pytest.mark.parametrize('df, func, expected', chain(_get_cython_table_params(DataFrame(), [('cumprod', DataFrame()), ('cumsum', DataFrame())]), _get_cython_table_params(DataFrame([[np.nan, 1], [1, 2]]), [('cumprod', DataFrame([[np.nan, 1], [1, 2]])), ('cumsum', DataFrame([[np.nan, 1], [1, 3]]))])))
def test_agg_cython_table_transform(self, df, func, expected, axis):
    if axis == 'columns' or axis == 1:
        expected = expected.astype('float64')
    result = df.agg(func, axis=axis)
    tm.assert_frame_equal(result, expected)