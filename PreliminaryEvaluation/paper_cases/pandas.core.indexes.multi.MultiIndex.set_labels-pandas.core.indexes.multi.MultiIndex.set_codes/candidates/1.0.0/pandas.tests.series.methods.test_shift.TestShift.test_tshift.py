def test_tshift(self, datetime_series):
    ps = tm.makePeriodSeries()
    shifted = ps.tshift(1)
    unshifted = shifted.tshift(-1)
    tm.assert_series_equal(unshifted, ps)
    shifted2 = ps.tshift(freq='B')
    tm.assert_series_equal(shifted, shifted2)
    shifted3 = ps.tshift(freq=BDay())
    tm.assert_series_equal(shifted, shifted3)
    msg = 'Given freq M does not match PeriodIndex freq B'
    with pytest.raises(ValueError, match=msg):
        ps.tshift(freq='M')
    shifted = datetime_series.tshift(1)
    unshifted = shifted.tshift(-1)
    tm.assert_series_equal(datetime_series, unshifted)
    shifted2 = datetime_series.tshift(freq=datetime_series.index.freq)
    tm.assert_series_equal(shifted, shifted2)
    inferred_ts = Series(datetime_series.values, Index(np.asarray(datetime_series.index)), name='ts')
    shifted = inferred_ts.tshift(1)
    unshifted = shifted.tshift(-1)
    tm.assert_series_equal(shifted, datetime_series.tshift(1))
    tm.assert_series_equal(unshifted, inferred_ts)
    no_freq = datetime_series[[0, 5, 7]]
    msg = 'Freq was not given and was not set in the index'
    with pytest.raises(ValueError, match=msg):
        no_freq.tshift()