def test_contains_nans(self):
    i = Float64Index([1.0, 2.0, np.nan])
    assert np.nan in i