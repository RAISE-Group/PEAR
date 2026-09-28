def test_array_from_scalars(self, data):
    scalars = [data[0], data[1], data[2]]
    result = data._from_sequence(scalars)
    assert isinstance(result, type(data))