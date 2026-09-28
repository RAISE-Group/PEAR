def test_copy(self, data):
    assert data[0] != data[1]
    result = data.copy()
    data[1] = data[0]
    assert result[1] != result[0]