def test_unicode_repr_level_names(self):
    index = MultiIndex.from_tuples([(0, 0), (1, 1)], names=['Δ', 'i1'])
    s = Series(range(2), index=index)
    df = DataFrame(np.random.randn(2, 4), index=index)
    repr(s)
    repr(df)