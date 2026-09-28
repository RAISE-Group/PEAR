def test_interp_bad_method(self):
    df = DataFrame({'A': [1, 2, np.nan, 4], 'B': [1, 4, 9, np.nan], 'C': [1, 2, 3, 5], 'D': list('abcd')})
    with pytest.raises(ValueError):
        df.interpolate(method='not_a_method')