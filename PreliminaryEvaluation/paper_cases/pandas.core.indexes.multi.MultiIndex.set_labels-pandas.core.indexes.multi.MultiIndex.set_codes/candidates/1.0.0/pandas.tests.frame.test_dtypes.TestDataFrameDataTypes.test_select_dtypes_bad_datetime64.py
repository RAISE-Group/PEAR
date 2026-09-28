def test_select_dtypes_bad_datetime64(self):
    df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
    with pytest.raises(ValueError, match='.+ is too specific'):
        df.select_dtypes(include=['datetime64[D]'])
    with pytest.raises(ValueError, match='.+ is too specific'):
        df.select_dtypes(exclude=['datetime64[as]'])