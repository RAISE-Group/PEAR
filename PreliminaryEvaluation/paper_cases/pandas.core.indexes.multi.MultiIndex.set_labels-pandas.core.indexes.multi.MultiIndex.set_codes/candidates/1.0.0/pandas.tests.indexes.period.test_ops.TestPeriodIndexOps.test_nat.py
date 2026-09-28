def test_nat(self):
    assert pd.PeriodIndex._na_value is NaT
    assert pd.PeriodIndex([], freq='M')._na_value is NaT
    idx = pd.PeriodIndex(['2011-01-01', '2011-01-02'], freq='D')
    assert idx._can_hold_na
    tm.assert_numpy_array_equal(idx._isnan, np.array([False, False]))
    assert idx.hasnans is False
    tm.assert_numpy_array_equal(idx._nan_idxs, np.array([], dtype=np.intp))
    idx = pd.PeriodIndex(['2011-01-01', 'NaT'], freq='D')
    assert idx._can_hold_na
    tm.assert_numpy_array_equal(idx._isnan, np.array([False, True]))
    assert idx.hasnans is True
    tm.assert_numpy_array_equal(idx._nan_idxs, np.array([1], dtype=np.intp))