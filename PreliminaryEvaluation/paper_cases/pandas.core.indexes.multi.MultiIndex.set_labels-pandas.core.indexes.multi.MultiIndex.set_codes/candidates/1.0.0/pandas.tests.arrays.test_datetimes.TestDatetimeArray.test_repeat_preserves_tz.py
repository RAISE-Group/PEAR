def test_repeat_preserves_tz(self):
    dti = pd.date_range('2000', periods=2, freq='D', tz='US/Central')
    arr = DatetimeArray(dti)
    repeated = arr.repeat([1, 1])
    expected = DatetimeArray(arr.asi8, freq=None, dtype=arr.dtype)
    tm.assert_equal(repeated, expected)