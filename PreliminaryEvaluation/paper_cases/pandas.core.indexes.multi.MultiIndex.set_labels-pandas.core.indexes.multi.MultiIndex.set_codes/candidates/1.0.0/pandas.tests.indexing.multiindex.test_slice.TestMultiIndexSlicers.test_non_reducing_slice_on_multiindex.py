def test_non_reducing_slice_on_multiindex(self):
    dic = {('a', 'd'): [1, 4], ('a', 'c'): [2, 3], ('b', 'c'): [3, 2], ('b', 'd'): [4, 1]}
    df = pd.DataFrame(dic, index=[0, 1])
    idx = pd.IndexSlice
    slice_ = idx[:, idx['b', 'd']]
    tslice_ = _non_reducing_slice(slice_)
    result = df.loc[tslice_]
    expected = pd.DataFrame({('b', 'd'): [4, 1]})
    tm.assert_frame_equal(result, expected)