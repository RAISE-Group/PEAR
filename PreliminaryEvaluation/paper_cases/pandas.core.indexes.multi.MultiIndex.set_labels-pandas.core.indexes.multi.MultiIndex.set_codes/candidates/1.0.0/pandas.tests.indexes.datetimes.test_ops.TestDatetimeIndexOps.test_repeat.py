def test_repeat(self, tz_naive_fixture):
    tz = tz_naive_fixture
    reps = 2
    msg = "the 'axis' parameter is not supported"
    rng = pd.date_range(start='2016-01-01', periods=2, freq='30Min', tz=tz)
    expected_rng = DatetimeIndex([Timestamp('2016-01-01 00:00:00', tz=tz, freq='30T'), Timestamp('2016-01-01 00:00:00', tz=tz, freq='30T'), Timestamp('2016-01-01 00:30:00', tz=tz, freq='30T'), Timestamp('2016-01-01 00:30:00', tz=tz, freq='30T')])
    res = rng.repeat(reps)
    tm.assert_index_equal(res, expected_rng)
    assert res.freq is None
    tm.assert_index_equal(np.repeat(rng, reps), expected_rng)
    with pytest.raises(ValueError, match=msg):
        np.repeat(rng, reps, axis=1)