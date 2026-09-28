def test_rolling_on_decreasing_index(self):
    index = [Timestamp('20190101 09:00:00'), Timestamp('20190101 09:00:02'), Timestamp('20190101 09:00:03'), Timestamp('20190101 09:00:05'), Timestamp('20190101 09:00:06')]
    df = DataFrame({'column': [3, 4, 4, 2, 1]}, index=reversed(index))
    result = df.rolling('2s').min()
    expected = DataFrame({'column': [3.0, 3.0, 3.0, 2.0, 1.0]}, index=reversed(index))
    tm.assert_frame_equal(result, expected)