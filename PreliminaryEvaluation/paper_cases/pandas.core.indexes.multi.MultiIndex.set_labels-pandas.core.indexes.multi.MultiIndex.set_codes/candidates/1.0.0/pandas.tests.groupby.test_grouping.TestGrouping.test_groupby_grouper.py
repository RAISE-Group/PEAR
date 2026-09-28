def test_groupby_grouper(self, df):
    grouped = df.groupby('A')
    result = df.groupby(grouped.grouper).mean()
    expected = grouped.mean()
    tm.assert_frame_equal(result, expected)