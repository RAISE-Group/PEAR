@pytest.mark.parametrize('tz', [None, 'US/Central'])
def test_to_datetime_dtarr(self, tz):
    dti = date_range('1965-04-03', periods=19, freq='2W', tz=tz)
    arr = DatetimeArray(dti)
    result = to_datetime(arr)
    assert result is arr
    result = to_datetime(arr)
    assert result is arr