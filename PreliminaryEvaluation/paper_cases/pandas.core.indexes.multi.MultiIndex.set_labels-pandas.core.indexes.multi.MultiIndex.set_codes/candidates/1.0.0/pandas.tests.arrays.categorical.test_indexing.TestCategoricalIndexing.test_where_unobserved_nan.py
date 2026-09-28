def test_where_unobserved_nan(self):
    ser = pd.Series(pd.Categorical(['a', 'b']))
    result = ser.where([True, False])
    expected = pd.Series(pd.Categorical(['a', None], categories=['a', 'b']))
    tm.assert_series_equal(result, expected)
    ser = pd.Series(pd.Categorical(['a', 'b']))
    result = ser.where([False, False])
    expected = pd.Series(pd.Categorical([None, None], categories=['a', 'b']))
    tm.assert_series_equal(result, expected)