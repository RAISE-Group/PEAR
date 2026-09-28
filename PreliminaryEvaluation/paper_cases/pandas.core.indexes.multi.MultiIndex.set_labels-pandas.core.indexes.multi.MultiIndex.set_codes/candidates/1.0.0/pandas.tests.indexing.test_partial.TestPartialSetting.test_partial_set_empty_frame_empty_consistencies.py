def test_partial_set_empty_frame_empty_consistencies(self):
    df = DataFrame(columns=['x', 'y'])
    df['x'] = [1, 2]
    expected = DataFrame(dict(x=[1, 2], y=[np.nan, np.nan]))
    tm.assert_frame_equal(df, expected, check_dtype=False)
    df = DataFrame(columns=['x', 'y'])
    df['x'] = ['1', '2']
    expected = DataFrame(dict(x=['1', '2'], y=[np.nan, np.nan]), dtype=object)
    tm.assert_frame_equal(df, expected)
    df = DataFrame(columns=['x', 'y'])
    df.loc[0, 'x'] = 1
    expected = DataFrame(dict(x=[1], y=[np.nan]))
    tm.assert_frame_equal(df, expected, check_dtype=False)