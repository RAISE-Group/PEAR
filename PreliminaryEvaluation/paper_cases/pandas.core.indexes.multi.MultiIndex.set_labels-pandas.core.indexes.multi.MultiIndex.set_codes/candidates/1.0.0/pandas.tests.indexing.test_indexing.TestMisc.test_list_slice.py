def test_list_slice(self):
    slices = [['A'], Series(['A']), np.array(['A'])]
    df = DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['A', 'B'])
    expected = pd.IndexSlice[:, ['A']]
    for subset in slices:
        result = _non_reducing_slice(subset)
        tm.assert_frame_equal(df.loc[result], df.loc[expected])