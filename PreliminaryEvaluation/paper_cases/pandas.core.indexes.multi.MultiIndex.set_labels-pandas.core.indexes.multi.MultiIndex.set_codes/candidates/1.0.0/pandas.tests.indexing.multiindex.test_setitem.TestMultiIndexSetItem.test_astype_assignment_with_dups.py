def test_astype_assignment_with_dups(self):
    cols = MultiIndex.from_tuples([('A', '1'), ('B', '1'), ('A', '2')])
    df = DataFrame(np.arange(3).reshape((1, 3)), columns=cols, dtype=object)
    index = df.index.copy()
    df['A'] = df['A'].astype(np.float64)
    tm.assert_index_equal(df.index, index)