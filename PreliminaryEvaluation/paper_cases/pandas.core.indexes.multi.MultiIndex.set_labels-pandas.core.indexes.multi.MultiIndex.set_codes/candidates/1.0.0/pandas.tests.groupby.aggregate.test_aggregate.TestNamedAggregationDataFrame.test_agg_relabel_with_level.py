def test_agg_relabel_with_level(self):
    df = pd.DataFrame({'A': [0, 0, 1, 1], 'B': [1, 2, 3, 4]}, index=pd.MultiIndex.from_product([['A', 'B'], ['a', 'b']]))
    result = df.groupby(level=0).agg(aa=('A', 'max'), bb=('A', 'min'), cc=('B', 'mean'))
    expected = pd.DataFrame({'aa': [0, 1], 'bb': [0, 1], 'cc': [1.5, 3.5]}, index=['A', 'B'])
    tm.assert_frame_equal(result, expected)