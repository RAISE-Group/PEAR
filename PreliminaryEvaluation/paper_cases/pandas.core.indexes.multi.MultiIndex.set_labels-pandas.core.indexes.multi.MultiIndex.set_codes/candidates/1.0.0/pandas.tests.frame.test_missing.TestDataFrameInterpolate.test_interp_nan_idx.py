def test_interp_nan_idx(self):
    df = DataFrame({'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, 4]})
    df = df.set_index('A')
    with pytest.raises(NotImplementedError):
        df.interpolate(method='values')