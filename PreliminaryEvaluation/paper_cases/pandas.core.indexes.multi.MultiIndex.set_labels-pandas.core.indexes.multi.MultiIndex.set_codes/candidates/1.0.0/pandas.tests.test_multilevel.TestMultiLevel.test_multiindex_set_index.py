def test_multiindex_set_index(self):
    d = {'t1': [2, 2.5, 3], 't2': [4, 5, 6]}
    df = DataFrame(d)
    tuples = [(0, 1), (0, 2), (1, 2)]
    df['tuples'] = tuples
    index = MultiIndex.from_tuples(df['tuples'])
    df.set_index(index)