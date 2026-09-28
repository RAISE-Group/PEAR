def test_constructor_bool(self):
    df = DataFrame({0: np.ones(10, dtype=bool), 1: np.zeros(10, dtype=bool)})
    assert df.values.dtype == np.bool_