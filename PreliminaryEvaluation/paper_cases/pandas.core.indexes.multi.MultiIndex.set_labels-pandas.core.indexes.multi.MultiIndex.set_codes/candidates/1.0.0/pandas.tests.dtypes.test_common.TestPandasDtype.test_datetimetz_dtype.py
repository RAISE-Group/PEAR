@pytest.mark.parametrize('dtype', ['datetime64[ns, US/Eastern]', 'datetime64[ns, Asia/Tokyo]', 'datetime64[ns, UTC]'])
def test_datetimetz_dtype(self, dtype):
    assert com.pandas_dtype(dtype) == DatetimeTZDtype.construct_from_string(dtype)
    assert com.pandas_dtype(dtype) == dtype