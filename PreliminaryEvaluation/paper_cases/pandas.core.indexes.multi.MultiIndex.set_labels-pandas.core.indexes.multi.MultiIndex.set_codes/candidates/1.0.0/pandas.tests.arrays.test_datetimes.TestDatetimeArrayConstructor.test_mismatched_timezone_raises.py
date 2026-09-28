def test_mismatched_timezone_raises(self):
    arr = DatetimeArray(np.array(['2000-01-01T06:00:00'], dtype='M8[ns]'), dtype=DatetimeTZDtype(tz='US/Central'))
    dtype = DatetimeTZDtype(tz='US/Eastern')
    with pytest.raises(TypeError, match='Timezone of the array'):
        DatetimeArray(arr, dtype=dtype)