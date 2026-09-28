def test_fillna_dict_series(self):
    df = DataFrame({'a': [np.nan, 1, 2, np.nan, np.nan], 'b': [1, 2, 3, np.nan, np.nan], 'c': [np.nan, 1, 2, 3, 4]})
    result = df.fillna({'a': 0, 'b': 5})
    expected = df.copy()
    expected['a'] = expected['a'].fillna(0)
    expected['b'] = expected['b'].fillna(5)
    tm.assert_frame_equal(result, expected)
    result = df.fillna({'a': 0, 'b': 5, 'd': 7})
    result = df.fillna(df.max())
    expected = df.fillna(df.max().to_dict())
    tm.assert_frame_equal(result, expected)
    with pytest.raises(NotImplementedError, match='column by column'):
        df.fillna(df.max(1), axis=1)