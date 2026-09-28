def test_where_unobserved_categories(self):
    ser = pd.Series(Categorical(['a', 'b', 'c'], categories=['d', 'c', 'b', 'a']))
    result = ser.where([True, True, False], other='b')
    expected = pd.Series(Categorical(['a', 'b', 'b'], categories=ser.cat.categories))
    tm.assert_series_equal(result, expected)