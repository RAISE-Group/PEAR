def test_arith_flex_series(self, simple_frame):
    df = simple_frame
    row = df.xs('a')
    col = df['two']
    ops = ['add', 'sub', 'mul', 'mod']
    for op in ops:
        f = getattr(df, op)
        op = getattr(operator, op)
        tm.assert_frame_equal(f(row), op(df, row))
        tm.assert_frame_equal(f(col, axis=0), op(df.T, col).T)
    tm.assert_frame_equal(df.add(row, axis=None), df + row)
    tm.assert_frame_equal(df.div(row), df / row)
    tm.assert_frame_equal(df.div(col, axis=0), (df.T / col).T)
    df = pd.DataFrame(np.arange(3 * 2).reshape((3, 2)), dtype='int64')
    expected = pd.DataFrame([[np.nan, np.inf], [1.0, 1.5], [1.0, 1.25]])
    result = df.div(df[0], axis='index')
    tm.assert_frame_equal(result, expected)
    df = pd.DataFrame(np.arange(3 * 2).reshape((3, 2)), dtype='float64')
    expected = pd.DataFrame([[np.nan, np.inf], [1.0, 1.5], [1.0, 1.25]])
    result = df.div(df[0], axis='index')
    tm.assert_frame_equal(result, expected)