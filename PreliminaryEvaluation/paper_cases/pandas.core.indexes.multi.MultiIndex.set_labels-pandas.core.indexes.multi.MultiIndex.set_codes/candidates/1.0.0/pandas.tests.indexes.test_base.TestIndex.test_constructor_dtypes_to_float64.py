@pytest.mark.parametrize('vals', [[1, 2, 3], [1.0, 2.0, 3.0], np.array([1.0, 2.0, 3.0]), np.array([1, 2, 3], dtype=int), np.array([1.0, 2.0, 3.0], dtype=float)])
def test_constructor_dtypes_to_float64(self, vals):
    index = Index(vals, dtype=float)
    assert isinstance(index, Float64Index)