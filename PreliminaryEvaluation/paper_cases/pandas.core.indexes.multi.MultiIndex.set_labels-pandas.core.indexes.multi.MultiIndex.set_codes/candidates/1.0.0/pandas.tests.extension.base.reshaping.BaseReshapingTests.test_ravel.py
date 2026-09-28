def test_ravel(self, data):
    result = data.ravel()
    assert type(result) == type(data)
    result[0] = result[1]
    assert data[0] == data[1]