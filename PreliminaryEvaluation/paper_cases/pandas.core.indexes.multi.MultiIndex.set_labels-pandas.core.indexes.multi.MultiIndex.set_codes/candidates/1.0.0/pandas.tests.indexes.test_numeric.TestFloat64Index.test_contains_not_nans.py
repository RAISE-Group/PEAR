def test_contains_not_nans(self):
    i = Float64Index([1.0, 2.0, np.nan])
    assert 1.0 in i