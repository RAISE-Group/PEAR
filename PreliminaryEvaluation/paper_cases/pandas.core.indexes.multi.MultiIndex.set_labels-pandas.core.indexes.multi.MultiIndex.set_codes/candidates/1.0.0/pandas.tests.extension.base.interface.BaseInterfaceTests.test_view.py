def test_view(self, data):
    assert data[1] != data[0]
    result = data.view()
    assert result is not data
    assert type(result) == type(data)
    result[1] = result[0]
    assert data[1] == data[0]
    data.view(dtype=None)