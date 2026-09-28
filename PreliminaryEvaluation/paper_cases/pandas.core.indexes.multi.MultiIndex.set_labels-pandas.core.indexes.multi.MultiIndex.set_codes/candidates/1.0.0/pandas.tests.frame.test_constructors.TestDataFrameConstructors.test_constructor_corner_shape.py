def test_constructor_corner_shape(self):
    df = DataFrame(index=[])
    assert df.values.shape == (0, 0)