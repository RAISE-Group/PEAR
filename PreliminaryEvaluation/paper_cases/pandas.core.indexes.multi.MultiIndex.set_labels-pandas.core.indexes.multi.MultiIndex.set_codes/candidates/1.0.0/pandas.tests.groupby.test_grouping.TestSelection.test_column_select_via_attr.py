def test_column_select_via_attr(self, df):
    result = df.groupby('A').C.sum()
    expected = df.groupby('A')['C'].sum()
    tm.assert_series_equal(result, expected)
    df['mean'] = 1.5
    result = df.groupby('A').mean()
    expected = df.groupby('A').agg(np.mean)
    tm.assert_frame_equal(result, expected)