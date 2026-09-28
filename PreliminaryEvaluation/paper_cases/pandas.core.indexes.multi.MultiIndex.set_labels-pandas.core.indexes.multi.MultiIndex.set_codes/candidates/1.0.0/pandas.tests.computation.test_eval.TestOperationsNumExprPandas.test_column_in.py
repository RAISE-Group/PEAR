def test_column_in(self):
    df = DataFrame({'a': [11], 'b': [-32]})
    result = df.eval('a in [11, -32]')
    expected = Series([True])
    tm.assert_series_equal(result, expected)