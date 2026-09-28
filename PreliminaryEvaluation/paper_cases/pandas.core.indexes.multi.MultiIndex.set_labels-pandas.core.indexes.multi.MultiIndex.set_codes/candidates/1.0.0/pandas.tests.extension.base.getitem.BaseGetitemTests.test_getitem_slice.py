def test_getitem_slice(self, data):
    result = data[slice(0)]
    assert isinstance(result, type(data))
    result = data[slice(1)]
    assert isinstance(result, type(data))