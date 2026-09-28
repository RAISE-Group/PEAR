def test_between_time(self, close_open_fixture):
    rng = date_range('1/1/2000', '1/5/2000', freq='5min')
    ts = DataFrame(np.random.randn(len(rng), 2), index=rng)
    stime = time(0, 0)
    etime = time(1, 0)
    inc_start, inc_end = close_open_fixture
    filtered = ts.between_time(stime, etime, inc_start, inc_end)
    exp_len = 13 * 4 + 1
    if not inc_start:
        exp_len -= 5
    if not inc_end:
        exp_len -= 4
    assert len(filtered) == exp_len
    for rs in filtered.index:
        t = rs.time()
        if inc_start:
            assert t >= stime
        else:
            assert t > stime
        if inc_end:
            assert t <= etime
        else:
            assert t < etime
    result = ts.between_time('00:00', '01:00')
    expected = ts.between_time(stime, etime)
    tm.assert_frame_equal(result, expected)
    rng = date_range('1/1/2000', '1/5/2000', freq='5min')
    ts = DataFrame(np.random.randn(len(rng), 2), index=rng)
    stime = time(22, 0)
    etime = time(9, 0)
    filtered = ts.between_time(stime, etime, inc_start, inc_end)
    exp_len = (12 * 11 + 1) * 4 + 1
    if not inc_start:
        exp_len -= 4
    if not inc_end:
        exp_len -= 4
    assert len(filtered) == exp_len
    for rs in filtered.index:
        t = rs.time()
        if inc_start:
            assert t >= stime or t <= etime
        else:
            assert t > stime or t <= etime
        if inc_end:
            assert t <= etime or t >= stime
        else:
            assert t < etime or t >= stime