def test_interp_raise_on_only_mixed(self):
    df = DataFrame({'A': [1, 2, np.nan, 4], 'B': ['a', 'b', 'c', 'd'], 'C': [np.nan, 2, 5, 7], 'D': [np.nan, np.nan, 9, 9], 'E': [1, 2, 3, 4]})
    with pytest.raises(TypeError):
        df.interpolate(axis=1)