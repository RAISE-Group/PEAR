def test_copy(self):
    data = np.array([1, 2, 3], dtype='m8[ns]')
    arr = TimedeltaArray(data, copy=False)
    assert arr._data is data
    arr = TimedeltaArray(data, copy=True)
    assert arr._data is not data
    assert arr._data.base is not data