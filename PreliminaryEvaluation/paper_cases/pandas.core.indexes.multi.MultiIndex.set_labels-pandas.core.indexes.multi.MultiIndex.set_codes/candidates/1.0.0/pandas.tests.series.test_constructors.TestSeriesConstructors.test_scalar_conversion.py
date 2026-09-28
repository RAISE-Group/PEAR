def test_scalar_conversion(self):
    scalar = Series(0.5)
    assert not isinstance(scalar, float)
    assert float(Series([1.0])) == 1.0
    assert int(Series([1.0])) == 1