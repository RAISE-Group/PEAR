def test_concat_same_type_invalid(self, datetime_index):
    dti = datetime_index
    arr = DatetimeArray(dti)
    if arr.tz is None:
        other = arr.tz_localize('UTC')
    else:
        other = arr.tz_localize(None)
    with pytest.raises(AssertionError):
        arr._concat_same_type([arr, other])