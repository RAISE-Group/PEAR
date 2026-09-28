def test_truncate(self, datetime_frame):
    ts = datetime_frame[::3]
    start, end = (datetime_frame.index[3], datetime_frame.index[6])
    start_missing = datetime_frame.index[2]
    end_missing = datetime_frame.index[7]
    truncated = ts.truncate()
    tm.assert_frame_equal(truncated, ts)
    expected = ts[1:3]
    truncated = ts.truncate(start, end)
    tm.assert_frame_equal(truncated, expected)
    truncated = ts.truncate(start_missing, end_missing)
    tm.assert_frame_equal(truncated, expected)
    expected = ts[1:]
    truncated = ts.truncate(before=start)
    tm.assert_frame_equal(truncated, expected)
    truncated = ts.truncate(before=start_missing)
    tm.assert_frame_equal(truncated, expected)
    expected = ts[:3]
    truncated = ts.truncate(after=end)
    tm.assert_frame_equal(truncated, expected)
    truncated = ts.truncate(after=end_missing)
    tm.assert_frame_equal(truncated, expected)
    msg = 'Truncate: 2000-01-06 00:00:00 must be after 2000-02-04 00:00:00'
    with pytest.raises(ValueError, match=msg):
        ts.truncate(before=ts.index[-1] - ts.index.freq, after=ts.index[0] + ts.index.freq)