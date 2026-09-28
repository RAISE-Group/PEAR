def test_crosstab_single(self):
    df = self.df
    result = crosstab(df['A'], df['C'])
    expected = df.groupby(['A', 'C']).size().unstack()
    tm.assert_frame_equal(result, expected.fillna(0).astype(np.int64))