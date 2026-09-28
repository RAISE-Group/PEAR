def test_where_subset(self):

    def f(x):
        return x > 0.5
    style1 = 'foo: bar'
    style2 = 'baz: foo'
    slices = [pd.IndexSlice[:], pd.IndexSlice[:, ['A']], pd.IndexSlice[[1], :], pd.IndexSlice[[1], ['A']], pd.IndexSlice[:2, ['A', 'B']]]
    for slice_ in slices:
        result = self.df.style.where(f, style1, style2, subset=slice_)._compute().ctx
        expected = {(r, c): [style1 if f(self.df.loc[row, col]) else style2] for r, row in enumerate(self.df.index) for c, col in enumerate(self.df.columns) if row in self.df.loc[slice_].index and col in self.df.loc[slice_].columns}
        assert result == expected