def test_quantile_axis_parameter(self):
    df = DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]}, index=[1, 2, 3])
    result = df.quantile(0.5, axis=0)
    expected = Series([2.0, 3.0], index=['A', 'B'], name=0.5)
    tm.assert_series_equal(result, expected)
    expected = df.quantile(0.5, axis='index')
    tm.assert_series_equal(result, expected)
    result = df.quantile(0.5, axis=1)
    expected = Series([1.5, 2.5, 3.5], index=[1, 2, 3], name=0.5)
    tm.assert_series_equal(result, expected)
    result = df.quantile(0.5, axis='columns')
    tm.assert_series_equal(result, expected)
    msg = "No axis named -1 for object type <class 'pandas.core.frame.DataFrame'>"
    with pytest.raises(ValueError, match=msg):
        df.quantile(0.1, axis=-1)
    msg = "No axis named column for object type <class 'pandas.core.frame.DataFrame'>"
    with pytest.raises(ValueError, match=msg):
        df.quantile(0.1, axis='column')