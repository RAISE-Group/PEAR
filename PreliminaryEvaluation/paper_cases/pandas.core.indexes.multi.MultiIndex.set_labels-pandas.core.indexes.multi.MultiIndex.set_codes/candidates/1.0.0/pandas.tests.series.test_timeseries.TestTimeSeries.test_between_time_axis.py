def test_between_time_axis(self):
    rng = date_range('1/1/2000', periods=100, freq='10min')
    ts = Series(np.random.randn(len(rng)), index=rng)
    stime, etime = ('08:00:00', '09:00:00')
    expected_length = 7
    assert len(ts.between_time(stime, etime)) == expected_length
    assert len(ts.between_time(stime, etime, axis=0)) == expected_length
    msg = "No axis named 1 for object type <class 'pandas.core.series.Series'>"
    with pytest.raises(ValueError, match=msg):
        ts.between_time(stime, etime, axis=1)