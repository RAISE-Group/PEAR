def test_nat(self, tz_naive_fixture):
    tz = tz_naive_fixture
    assert pd.DatetimeIndex._na_value is pd.NaT
    assert pd.DatetimeIndex([])._na_value is pd.NaT
    idx = pd.DatetimeIndex(['2011-01-01', '2011-01-02'], tz=tz)
    assert idx._can_hold_na
    tm.assert_numpy_array_equal(idx._isnan, np.array([False, False]))
    assert idx.hasnans is False
    tm.assert_numpy_array_equal(idx._nan_idxs, np.array([], dtype=np.intp))
    idx = pd.DatetimeIndex(['2011-01-01', 'NaT'], tz=tz)
    assert idx._can_hold_na
    tm.assert_numpy_array_equal(idx._isnan, np.array([False, True]))
    assert idx.hasnans is True
    tm.assert_numpy_array_equal(idx._nan_idxs, np.array([1], dtype=np.intp))