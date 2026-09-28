def test_getitem_scalar(self, data):
    result = data[0]
    assert isinstance(result, data.dtype.type)
    result = pd.Series(data)[0]
    assert isinstance(result, data.dtype.type)