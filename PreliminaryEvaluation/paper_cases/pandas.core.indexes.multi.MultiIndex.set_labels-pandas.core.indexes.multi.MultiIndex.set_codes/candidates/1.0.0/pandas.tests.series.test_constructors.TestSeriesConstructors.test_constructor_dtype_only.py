@pytest.mark.parametrize('dtype', ['f8', 'i8', 'M8[ns]', 'm8[ns]', 'category', 'object', 'datetime64[ns, UTC]'])
@pytest.mark.parametrize('index', [None, pd.Index([])])
def test_constructor_dtype_only(self, dtype, index):
    result = pd.Series(dtype=dtype, index=index)
    assert result.dtype == dtype
    assert len(result) == 0