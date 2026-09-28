def test_first_last_valid(self, datetime_series):
    ts = datetime_series.copy()
    ts[:5] = np.NaN
    index = ts.first_valid_index()
    assert index == ts.index[5]
    ts[-5:] = np.NaN
    index = ts.last_valid_index()
    assert index == ts.index[-6]
    ts[:] = np.nan
    assert ts.last_valid_index() is None
    assert ts.first_valid_index() is None
    ser = Series([], index=[], dtype=object)
    assert ser.last_valid_index() is None
    assert ser.first_valid_index() is None
    empty = Series(dtype=object)
    assert empty.last_valid_index() is None
    assert empty.first_valid_index() is None
    ts.index = date_range('20110101', periods=len(ts), freq='B')
    ts.iloc[1] = 1
    ts.iloc[-2] = 1
    assert ts.first_valid_index() == ts.index[1]
    assert ts.last_valid_index() == ts.index[-2]
    assert ts.first_valid_index().freq == ts.index.freq
    assert ts.last_valid_index().freq == ts.index.freq