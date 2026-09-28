def test_reindex_positional_warns(self):
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected = pd.DataFrame({'A': [1.0, 2], 'B': [4.0, 5], 'C': [np.nan, np.nan]})
    with tm.assert_produces_warning(FutureWarning):
        result = df.reindex([0, 1], ['A', 'B', 'C'])
    tm.assert_frame_equal(result, expected)