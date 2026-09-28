@pytest.mark.parametrize('key, pos', [([2, 4], [0, 1]), ([2], []), ([2, 3], [])])
def test_loc_multiindex_list_missing_label(self, key, pos):
    df = DataFrame(np.random.randn(3, 3), columns=[[2, 2, 4], [6, 8, 10]], index=[[4, 4, 8], [8, 10, 12]])
    expected = df.iloc[pos]
    result = df.loc[key]
    tm.assert_frame_equal(result, expected)