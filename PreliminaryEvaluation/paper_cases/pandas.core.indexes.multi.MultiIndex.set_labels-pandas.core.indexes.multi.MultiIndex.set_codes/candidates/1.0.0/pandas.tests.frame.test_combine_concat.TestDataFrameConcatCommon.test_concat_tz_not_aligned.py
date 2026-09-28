def test_concat_tz_not_aligned(self):
    ts = pd.to_datetime([1, 2]).tz_localize('UTC')
    a = pd.DataFrame({'A': ts})
    b = pd.DataFrame({'A': ts, 'B': ts})
    result = pd.concat([a, b], sort=True, ignore_index=True)
    expected = pd.DataFrame({'A': list(ts) + list(ts), 'B': [pd.NaT, pd.NaT] + list(ts)})
    tm.assert_frame_equal(result, expected)