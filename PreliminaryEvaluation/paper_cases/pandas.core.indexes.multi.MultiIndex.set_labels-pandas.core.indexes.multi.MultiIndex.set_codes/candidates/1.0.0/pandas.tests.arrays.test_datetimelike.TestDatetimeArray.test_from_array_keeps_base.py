def test_from_array_keeps_base(self):
    arr = np.array(['2000-01-01', '2000-01-02'], dtype='M8[ns]')
    dta = DatetimeArray(arr)
    assert dta._data is arr
    dta = DatetimeArray(arr[:0])
    assert dta._data.base is arr