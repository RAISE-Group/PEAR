def test_mixed_timedelta_datetime(self):
    frame = DataFrame({'a': [timedelta(23), pd.Timestamp('20130101')]}, dtype=object)
    expected = DataFrame({'a': [pd.Timedelta(frame.a[0]).value, pd.Timestamp(frame.a[1]).value]})
    result = pd.read_json(frame.to_json(date_unit='ns'), dtype={'a': 'int64'})
    tm.assert_frame_equal(result, expected, check_index_type=False)