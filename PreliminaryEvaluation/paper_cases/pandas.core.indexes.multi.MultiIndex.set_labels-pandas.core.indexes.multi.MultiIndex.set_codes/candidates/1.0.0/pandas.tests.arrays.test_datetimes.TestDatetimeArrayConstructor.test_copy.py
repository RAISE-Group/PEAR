def test_copy(self):
    data = np.array([1, 2, 3], dtype='M8[ns]')
    arr = DatetimeArray(data, copy=False)
    assert arr._data is data
    arr = DatetimeArray(data, copy=True)
    assert arr._data is not data