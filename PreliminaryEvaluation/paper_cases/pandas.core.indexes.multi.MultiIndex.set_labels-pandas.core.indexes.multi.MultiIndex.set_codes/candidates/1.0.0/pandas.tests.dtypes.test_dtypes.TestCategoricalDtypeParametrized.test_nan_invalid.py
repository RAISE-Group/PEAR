def test_nan_invalid(self):
    with pytest.raises(ValueError):
        CategoricalDtype([1, 2, np.nan])