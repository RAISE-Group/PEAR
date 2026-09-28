def test_nonunique_assignment_1750(self):
    df = DataFrame([[1, 1, 'x', 'X'], [1, 1, 'y', 'Y'], [1, 2, 'z', 'Z']], columns=list('ABCD'))
    df = df.set_index(['A', 'B'])
    ix = MultiIndex.from_tuples([(1, 1)])
    df.loc[ix, 'C'] = '_'
    assert (df.xs((1, 1))['C'] == '_').all()