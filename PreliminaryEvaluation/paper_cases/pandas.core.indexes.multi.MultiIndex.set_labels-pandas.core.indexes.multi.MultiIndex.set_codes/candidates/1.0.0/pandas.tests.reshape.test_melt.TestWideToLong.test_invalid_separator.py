def test_invalid_separator(self):
    sep = 'nope!'
    df = pd.DataFrame({'A2010': [1.0, 2.0], 'A2011': [3.0, 4.0], 'B2010': [5.0, 6.0], 'X': ['X1', 'X2']})
    df['id'] = df.index
    exp_data = {'X': '', 'A2010': [], 'A2011': [], 'B2010': [], 'id': [], 'year': [], 'A': [], 'B': []}
    expected = pd.DataFrame(exp_data).astype({'year': 'int'})
    expected = expected.set_index(['id', 'year'])[['X', 'A2010', 'A2011', 'B2010', 'A', 'B']]
    expected.index.set_levels([0, 1], level=0, inplace=True)
    result = wide_to_long(df, ['A', 'B'], i='id', j='year', sep=sep)
    tm.assert_frame_equal(result.sort_index(axis=1), expected.sort_index(axis=1))