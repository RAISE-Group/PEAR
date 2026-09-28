def test_astype_to_same(self):
    arr = DatetimeArray._from_sequence(['2000'], tz='US/Central')
    result = arr.astype(DatetimeTZDtype(tz='US/Central'), copy=False)
    assert result is arr