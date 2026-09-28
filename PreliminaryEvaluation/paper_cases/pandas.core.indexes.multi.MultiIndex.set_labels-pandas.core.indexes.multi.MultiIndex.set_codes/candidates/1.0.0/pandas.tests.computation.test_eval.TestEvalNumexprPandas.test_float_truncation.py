def test_float_truncation(self):
    exp = '1000000000.006'
    result = pd.eval(exp, engine=self.engine, parser=self.parser)
    expected = np.float64(exp)
    assert result == expected
    df = pd.DataFrame({'A': [1000000000.0009, 1000000000.0011, 1000000000.0015]})
    cutoff = 1000000000.0006
    result = df.query(f'A < {cutoff:.4f}')
    assert result.empty
    cutoff = 1000000000.001
    result = df.query(f'A > {cutoff:.4f}')
    expected = df.loc[[1, 2], :]
    tm.assert_frame_equal(expected, result)
    exact = 1000000000.0011
    result = df.query(f'A == {exact:.4f}')
    expected = df.loc[[1], :]
    tm.assert_frame_equal(expected, result)