def test_centered_axis_validation(self):
    Series(np.ones(10)).rolling(window=3, center=True, axis=0).mean()
    with pytest.raises(ValueError):
        Series(np.ones(10)).rolling(window=3, center=True, axis=1).mean()
    DataFrame(np.ones((10, 10))).rolling(window=3, center=True, axis=0).mean()
    DataFrame(np.ones((10, 10))).rolling(window=3, center=True, axis=1).mean()
    with pytest.raises(ValueError):
        DataFrame(np.ones((10, 10))).rolling(window=3, center=True, axis=2).mean()