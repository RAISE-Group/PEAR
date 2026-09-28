def test_where_other_categorical(self):
    ser = pd.Series(Categorical(['a', 'b', 'c'], categories=['d', 'c', 'b', 'a']))
    other = Categorical(['b', 'c', 'a'], categories=['a', 'c', 'b', 'd'])
    result = ser.where([True, False, True], other)
    expected = pd.Series(Categorical(['a', 'c', 'c'], dtype=ser.dtype))
    tm.assert_series_equal(result, expected)