def test_categorical_nan_only_columns(self, setup_path):
    df = pd.DataFrame({'a': ['a', 'b', 'c', np.nan], 'b': [np.nan, np.nan, np.nan, np.nan], 'c': [1, 2, 3, 4], 'd': pd.Series([None] * 4, dtype=object)})
    df['a'] = df.a.astype('category')
    df['b'] = df.b.astype('category')
    df['d'] = df.b.astype('category')
    expected = df
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', format='table', data_columns=True)
        result = read_hdf(path, 'df')
        tm.assert_frame_equal(result, expected)