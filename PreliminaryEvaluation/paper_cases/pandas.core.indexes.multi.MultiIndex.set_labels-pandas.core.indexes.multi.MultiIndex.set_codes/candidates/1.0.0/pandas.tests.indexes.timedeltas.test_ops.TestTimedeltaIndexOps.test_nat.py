def test_nat(self):
    assert pd.TimedeltaIndex._na_value is pd.NaT
    assert pd.TimedeltaIndex([])._na_value is pd.NaT
    idx = pd.TimedeltaIndex(['1 days', '2 days'])
    assert idx._can_hold_na
    tm.assert_numpy_array_equal(idx._isnan, np.array([False, False]))
    assert idx.hasnans is False
    tm.assert_numpy_array_equal(idx._nan_idxs, np.array([], dtype=np.intp))
    idx = pd.TimedeltaIndex(['1 days', 'NaT'])
    assert idx._can_hold_na
    tm.assert_numpy_array_equal(idx._isnan, np.array([False, True]))
    assert idx.hasnans is True
    tm.assert_numpy_array_equal(idx._nan_idxs, np.array([1], dtype=np.intp))