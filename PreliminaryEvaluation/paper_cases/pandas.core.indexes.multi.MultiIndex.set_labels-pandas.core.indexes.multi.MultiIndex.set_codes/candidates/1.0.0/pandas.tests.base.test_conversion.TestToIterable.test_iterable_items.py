@pytest.mark.parametrize('dtype, rdtype', dtypes)
def test_iterable_items(self, dtype, rdtype):
    s = Series([1], dtype=dtype)
    _, result = list(s.items())[0]
    assert isinstance(result, rdtype)
    _, result = list(s.items())[0]
    assert isinstance(result, rdtype)