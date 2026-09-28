def test_pivot_with_categorical(self, observed, ordered_fixture):
    idx = [np.nan, 'low', 'high', 'low', np.nan]
    col = [np.nan, 'A', 'B', np.nan, 'A']
    df = pd.DataFrame({'In': pd.Categorical(idx, categories=['low', 'high'], ordered=ordered_fixture), 'Col': pd.Categorical(col, categories=['A', 'B'], ordered=ordered_fixture), 'Val': range(1, 6)})
    result = df.pivot_table(index='In', columns='Col', values='Val', observed=observed)
    expected_cols = pd.CategoricalIndex(['A', 'B'], ordered=ordered_fixture, name='Col')
    expected = pd.DataFrame(data=[[2.0, np.nan], [np.nan, 3.0]], columns=expected_cols)
    expected.index = Index(pd.Categorical(['low', 'high'], categories=['low', 'high'], ordered=ordered_fixture), name='In')
    tm.assert_frame_equal(result, expected)
    result = df.pivot_table(columns='Col', values='Val', observed=observed)
    expected = pd.DataFrame(data=[[3.5, 3.0]], columns=expected_cols, index=Index(['Val']))
    tm.assert_frame_equal(result, expected)