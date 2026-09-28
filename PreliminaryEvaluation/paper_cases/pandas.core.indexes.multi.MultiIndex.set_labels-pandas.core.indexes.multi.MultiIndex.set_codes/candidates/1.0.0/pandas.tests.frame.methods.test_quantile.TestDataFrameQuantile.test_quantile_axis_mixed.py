def test_quantile_axis_mixed(self):
    df = DataFrame({'A': [1, 2, 3], 'B': [2.0, 3.0, 4.0], 'C': pd.date_range('20130101', periods=3), 'D': ['foo', 'bar', 'baz']})
    result = df.quantile(0.5, axis=1)
    expected = Series([1.5, 2.5, 3.5], name=0.5)
    tm.assert_series_equal(result, expected)
    with pytest.raises(TypeError):
        df.quantile(0.5, axis=1, numeric_only=False)