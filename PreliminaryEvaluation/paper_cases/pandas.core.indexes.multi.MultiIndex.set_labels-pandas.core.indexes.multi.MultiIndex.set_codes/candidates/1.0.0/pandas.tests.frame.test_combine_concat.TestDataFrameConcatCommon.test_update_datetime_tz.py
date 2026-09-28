def test_update_datetime_tz(self):
    result = DataFrame([pd.Timestamp('2019', tz='UTC')])
    result.update(result)
    expected = DataFrame([pd.Timestamp('2019', tz='UTC')])
    tm.assert_frame_equal(result, expected)