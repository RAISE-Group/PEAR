def test_at_time(self):
    rng = date_range('1/1/2000', '1/5/2000', freq='5min')
    ts = DataFrame(np.random.randn(len(rng), 2), index=rng)
    rs = ts.at_time(rng[1])
    assert (rs.index.hour == rng[1].hour).all()
    assert (rs.index.minute == rng[1].minute).all()
    assert (rs.index.second == rng[1].second).all()
    result = ts.at_time('9:30')
    expected = ts.at_time(time(9, 30))
    tm.assert_frame_equal(result, expected)
    result = ts.loc[time(9, 30)]
    expected = ts.loc[(rng.hour == 9) & (rng.minute == 30)]
    tm.assert_frame_equal(result, expected)
    rng = date_range('1/1/2000', '1/31/2000')
    ts = DataFrame(np.random.randn(len(rng), 3), index=rng)
    result = ts.at_time(time(0, 0))
    tm.assert_frame_equal(result, ts)
    rng = date_range('1/1/2012', freq='23Min', periods=384)
    ts = DataFrame(np.random.randn(len(rng), 2), rng)
    rs = ts.at_time('16:00')
    assert len(rs) == 0