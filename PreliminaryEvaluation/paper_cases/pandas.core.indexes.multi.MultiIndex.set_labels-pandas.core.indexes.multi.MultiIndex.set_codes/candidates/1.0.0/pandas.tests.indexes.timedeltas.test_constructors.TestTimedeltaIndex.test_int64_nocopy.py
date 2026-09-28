def test_int64_nocopy(self):
    arr = np.arange(10, dtype=np.int64)
    tdi = TimedeltaIndex(arr, copy=False)
    assert tdi._data._data.base is arr