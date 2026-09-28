def test_non_reducing_slice(self):
    df = DataFrame([[0, 1], [2, 3]])
    slices = [pd.IndexSlice[:, 1], pd.IndexSlice[1, :], pd.IndexSlice[[1], [1]], pd.IndexSlice[1, [1]], pd.IndexSlice[[1], 1], pd.IndexSlice[1], pd.IndexSlice[1, 1], slice(None, None, None), [0, 1], np.array([0, 1]), Series([0, 1])]
    for slice_ in slices:
        tslice_ = _non_reducing_slice(slice_)
        assert isinstance(df.loc[tslice_], DataFrame)