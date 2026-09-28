def test_skip_sum_object_raises(self):
    df = DataFrame({'A': range(5), 'B': range(5, 10), 'C': 'foo'})
    r = df.rolling(window=3)
    result = r.sum()
    expected = DataFrame({'A': [np.nan, np.nan, 3, 6, 9], 'B': [np.nan, np.nan, 18, 21, 24]}, columns=list('AB'))
    tm.assert_frame_equal(result, expected)