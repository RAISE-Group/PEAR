def test_shift2(self):
    ts = Series(np.random.randn(5), index=date_range('1/1/2000', periods=5, freq='H'))
    result = ts.shift(1, freq='5T')
    exp_index = ts.index.shift(1, freq='5T')
    tm.assert_index_equal(result.index, exp_index)
    result = ts.shift(1, freq='4H')
    exp_index = ts.index + offsets.Hour(4)
    tm.assert_index_equal(result.index, exp_index)
    idx = DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-04'])
    msg = 'Cannot shift with no freq'
    with pytest.raises(NullFrequencyError, match=msg):
        idx.shift(1)