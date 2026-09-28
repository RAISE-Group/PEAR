def test_assign_index_sequences(self):
    df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}).set_index(['a', 'b'])
    index = list(df.index)
    index[0] = ('faz', 'boo')
    df.index = index
    repr(df)
    index[0] = ['faz', 'boo']
    df.index = index
    repr(df)