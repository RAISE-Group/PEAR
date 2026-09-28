def test_applymap_subset(self):

    def f(x):
        return 'foo: bar'
    slices = [pd.IndexSlice[:], pd.IndexSlice[:, ['A']], pd.IndexSlice[[1], :], pd.IndexSlice[[1], ['A']], pd.IndexSlice[:2, ['A', 'B']]]
    for slice_ in slices:
        result = self.df.style.applymap(f, subset=slice_)._compute().ctx
        expected = {(r, c): ['foo: bar'] for r, row in enumerate(self.df.index) for c, col in enumerate(self.df.columns) if row in self.df.loc[slice_].index and col in self.df.loc[slice_].columns}
        assert result == expected