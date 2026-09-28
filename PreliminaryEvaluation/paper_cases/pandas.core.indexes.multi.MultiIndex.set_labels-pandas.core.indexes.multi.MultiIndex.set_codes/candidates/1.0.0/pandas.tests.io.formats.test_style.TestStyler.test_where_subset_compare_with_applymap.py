def test_where_subset_compare_with_applymap(self):

    def f(x):
        return x > 0.5
    style1 = 'foo: bar'
    style2 = 'baz: foo'

    def g(x):
        return style1 if f(x) else style2
    slices = [pd.IndexSlice[:], pd.IndexSlice[:, ['A']], pd.IndexSlice[[1], :], pd.IndexSlice[[1], ['A']], pd.IndexSlice[:2, ['A', 'B']]]
    for slice_ in slices:
        result = self.df.style.where(f, style1, style2, subset=slice_)._compute().ctx
        expected = self.df.style.applymap(g, subset=slice_)._compute().ctx
        assert result == expected