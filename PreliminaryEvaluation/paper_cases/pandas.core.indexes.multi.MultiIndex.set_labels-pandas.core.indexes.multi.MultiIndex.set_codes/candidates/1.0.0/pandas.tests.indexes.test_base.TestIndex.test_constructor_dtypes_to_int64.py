@pytest.mark.parametrize('vals', [[1, 2, 3], np.array([1, 2, 3]), np.array([1, 2, 3], dtype=int), [1.0, 2.0, 3.0], np.array([1.0, 2.0, 3.0], dtype=float)])
def test_constructor_dtypes_to_int64(self, vals):
    index = Index(vals, dtype=int)
    assert isinstance(index, Int64Index)