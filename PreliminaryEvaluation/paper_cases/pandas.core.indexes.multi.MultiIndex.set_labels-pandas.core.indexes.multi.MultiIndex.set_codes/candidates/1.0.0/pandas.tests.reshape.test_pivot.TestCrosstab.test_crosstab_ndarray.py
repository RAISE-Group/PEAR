def test_crosstab_ndarray(self):
    a = np.random.randint(0, 5, size=100)
    b = np.random.randint(0, 3, size=100)
    c = np.random.randint(0, 10, size=100)
    df = DataFrame({'a': a, 'b': b, 'c': c})
    result = crosstab(a, [b, c], rownames=['a'], colnames=('b', 'c'))
    expected = crosstab(df['a'], [df['b'], df['c']])
    tm.assert_frame_equal(result, expected)
    result = crosstab([b, c], a, colnames=['a'], rownames=('b', 'c'))
    expected = crosstab([df['b'], df['c']], df['a'])
    tm.assert_frame_equal(result, expected)
    result = crosstab(self.df['A'].values, self.df['C'].values)
    assert result.index.name == 'row_0'
    assert result.columns.name == 'col_0'