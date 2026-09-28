def test_replace_with_empty_dictlike(self, mix_abc):
    df = DataFrame(mix_abc)
    tm.assert_frame_equal(df, df.replace({}))
    tm.assert_frame_equal(df, df.replace(Series([], dtype=object)))
    tm.assert_frame_equal(df, df.replace({'b': {}}))
    tm.assert_frame_equal(df, df.replace(Series({'b': {}})))