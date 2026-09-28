def test_merge_groupby_multiple_column_with_categorical_column(self):
    df = pd.DataFrame({'x': [0], 'y': [0], 'z': pd.Categorical([0])})
    result = merge_asof(df, df, on='x', by=['y', 'z'])
    expected = pd.DataFrame({'x': [0], 'y': [0], 'z': pd.Categorical([0])})
    tm.assert_frame_equal(result, expected)