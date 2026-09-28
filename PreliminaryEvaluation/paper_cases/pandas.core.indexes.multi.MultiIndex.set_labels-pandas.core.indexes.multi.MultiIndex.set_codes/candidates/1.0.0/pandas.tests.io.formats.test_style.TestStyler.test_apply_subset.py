def test_apply_subset(self):
    axes = [0, 1]
    slices = [pd.IndexSlice[:], pd.IndexSlice[:, ['A']], pd.IndexSlice[[1], :], pd.IndexSlice[[1], ['A']], pd.IndexSlice[:2, ['A', 'B']]]
    for ax in axes:
        for slice_ in slices:
            result = self.df.style.apply(self.h, axis=ax, subset=slice_, foo='baz')._compute().ctx
            expected = {(r, c): ['color: baz'] for r, row in enumerate(self.df.index) for c, col in enumerate(self.df.columns) if row in self.df.loc[slice_].index and col in self.df.loc[slice_].columns}
            assert result == expected