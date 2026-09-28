def test_ufunc_coercions(self):
    idx = date_range('2011-01-01', periods=3, freq='2D', name='x')
    delta = np.timedelta64(1, 'D')
    exp = date_range('2011-01-02', periods=3, freq='2D', name='x')
    for result in [idx + delta, np.add(idx, delta)]:
        assert isinstance(result, DatetimeIndex)
        tm.assert_index_equal(result, exp)
        assert result.freq == '2D'
    exp = date_range('2010-12-31', periods=3, freq='2D', name='x')
    for result in [idx - delta, np.subtract(idx, delta)]:
        assert isinstance(result, DatetimeIndex)
        tm.assert_index_equal(result, exp)
        assert result.freq == '2D'
    delta = np.array([np.timedelta64(1, 'D'), np.timedelta64(2, 'D'), np.timedelta64(3, 'D')])
    exp = DatetimeIndex(['2011-01-02', '2011-01-05', '2011-01-08'], freq='3D', name='x')
    for result in [idx + delta, np.add(idx, delta)]:
        assert isinstance(result, DatetimeIndex)
        tm.assert_index_equal(result, exp)
        assert result.freq == '3D'
    exp = DatetimeIndex(['2010-12-31', '2011-01-01', '2011-01-02'], freq='D', name='x')
    for result in [idx - delta, np.subtract(idx, delta)]:
        assert isinstance(result, DatetimeIndex)
        tm.assert_index_equal(result, exp)
        assert result.freq == 'D'