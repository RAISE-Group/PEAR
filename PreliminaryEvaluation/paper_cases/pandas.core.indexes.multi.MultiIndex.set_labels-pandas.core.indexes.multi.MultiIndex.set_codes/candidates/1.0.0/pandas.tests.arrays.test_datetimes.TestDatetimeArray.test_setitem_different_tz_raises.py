def test_setitem_different_tz_raises(self):
    data = np.array([1, 2, 3], dtype='M8[ns]')
    arr = DatetimeArray(data, copy=False, dtype=DatetimeTZDtype(tz='US/Central'))
    with pytest.raises(TypeError, match='Cannot compare tz-naive and tz-aware'):
        arr[0] = pd.Timestamp('2000')
    with pytest.raises(ValueError, match='US/Central'):
        arr[0] = pd.Timestamp('2000', tz='US/Eastern')