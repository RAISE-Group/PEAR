def test_closed(self):
    df = DataFrame({'A': [1] * 5}, index=[Timestamp('20130101 09:00:01'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:04'), Timestamp('20130101 09:00:06')])
    with pytest.raises(ValueError):
        self.regular.rolling(window='2s', closed='blabla')
    expected = df.copy()
    expected['A'] = [1.0, 2, 2, 2, 1]
    result = df.rolling('2s', closed='right').sum()
    tm.assert_frame_equal(result, expected)
    result = df.rolling('2s').sum()
    tm.assert_frame_equal(result, expected)
    expected = df.copy()
    expected['A'] = [1.0, 2, 3, 3, 2]
    result = df.rolling('2s', closed='both').sum()
    tm.assert_frame_equal(result, expected)
    expected = df.copy()
    expected['A'] = [np.nan, 1.0, 2, 2, 1]
    result = df.rolling('2s', closed='left').sum()
    tm.assert_frame_equal(result, expected)
    expected = df.copy()
    expected['A'] = [np.nan, 1.0, 1, 1, np.nan]
    result = df.rolling('2s', closed='neither').sum()
    tm.assert_frame_equal(result, expected)