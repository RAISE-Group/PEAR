@pytest.mark.parametrize('method', ['sum', 'mean', 'prod', 'var', 'std', 'skew', 'min', 'max'])
def test_stat_operators_attempt_obj_array(self, method):
    data = {'a': [-0.0004998754019959134, -0.001646725777291983, 0.0006769587077588301], 'b': [-0, -0, 0.0], 'c': [0.00031111847529610595, 0.0014902627951905339, -0.0009409920003597969]}
    df1 = DataFrame(data, index=['foo', 'bar', 'baz'], dtype='O')
    df2 = DataFrame({0: [np.nan, 2], 1: [np.nan, 3], 2: [np.nan, 4]}, dtype=object)
    for df in [df1, df2]:
        assert df.values.dtype == np.object_
        result = getattr(df, method)(1)
        expected = getattr(df.astype('f8'), method)(1)
        if method in ['sum', 'prod']:
            tm.assert_series_equal(result, expected)