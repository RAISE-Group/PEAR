def test_join_dups(self):
    df = concat([DataFrame(np.random.randn(10, 4), columns=['A', 'A', 'B', 'B']), DataFrame(np.random.randint(0, 10, size=20).reshape(10, 2), columns=['A', 'C'])], axis=1)
    expected = concat([df, df], axis=1)
    result = df.join(df, rsuffix='_2')
    result.columns = expected.columns
    tm.assert_frame_equal(result, expected)
    w = DataFrame(np.random.randn(4, 2), columns=['x', 'y'])
    x = DataFrame(np.random.randn(4, 2), columns=['x', 'y'])
    y = DataFrame(np.random.randn(4, 2), columns=['x', 'y'])
    z = DataFrame(np.random.randn(4, 2), columns=['x', 'y'])
    dta = x.merge(y, left_index=True, right_index=True).merge(z, left_index=True, right_index=True, how='outer')
    dta = dta.merge(w, left_index=True, right_index=True)
    expected = concat([x, y, z, w], axis=1)
    expected.columns = ['x_x', 'y_x', 'x_y', 'y_y', 'x_x', 'y_x', 'x_y', 'y_y']
    tm.assert_frame_equal(dta, expected)