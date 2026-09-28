def test_to_period_nofreq(self):
    idx = DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-04'])
    with pytest.raises(ValueError):
        idx.to_period()
    idx = DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03'], freq='infer')
    assert idx.freqstr == 'D'
    expected = pd.PeriodIndex(['2000-01-01', '2000-01-02', '2000-01-03'], freq='D')
    tm.assert_index_equal(idx.to_period(), expected)
    idx = DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03'])
    assert idx.freqstr is None
    tm.assert_index_equal(idx.to_period(), expected)