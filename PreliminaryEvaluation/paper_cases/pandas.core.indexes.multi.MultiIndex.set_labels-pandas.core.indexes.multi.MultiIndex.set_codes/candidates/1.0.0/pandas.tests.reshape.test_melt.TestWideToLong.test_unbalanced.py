def test_unbalanced(self):
    df = pd.DataFrame({'A2010': [1.0, 2.0], 'A2011': [3.0, 4.0], 'B2010': [5.0, 6.0], 'X': ['X1', 'X2']})
    df['id'] = df.index
    exp_data = {'X': ['X1', 'X1', 'X2', 'X2'], 'A': [1.0, 3.0, 2.0, 4.0], 'B': [5.0, np.nan, 6.0, np.nan], 'id': [0, 0, 1, 1], 'year': [2010, 2011, 2010, 2011]}
    expected = pd.DataFrame(exp_data)
    expected = expected.set_index(['id', 'year'])[['X', 'A', 'B']]
    result = wide_to_long(df, ['A', 'B'], i='id', j='year')
    tm.assert_frame_equal(result, expected)