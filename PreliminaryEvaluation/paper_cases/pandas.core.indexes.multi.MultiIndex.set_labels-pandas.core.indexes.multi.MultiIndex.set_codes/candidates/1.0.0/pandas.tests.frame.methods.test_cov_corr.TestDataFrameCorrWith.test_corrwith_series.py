def test_corrwith_series(self, datetime_frame):
    result = datetime_frame.corrwith(datetime_frame['A'])
    expected = datetime_frame.apply(datetime_frame['A'].corr)
    tm.assert_series_equal(result, expected)