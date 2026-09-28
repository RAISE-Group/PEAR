def test_ops(self):
    for n in [4, 4000]:
        df = DataFrame(1, index=range(n), columns=list('abcd'))
        df.iloc[0] = 2
        m = df.mean()
        for op_str, op, rop in [('+', '__add__', '__radd__'), ('-', '__sub__', '__rsub__'), ('*', '__mul__', '__rmul__'), ('/', '__truediv__', '__rtruediv__')]:
            base = DataFrame(np.tile(m.values, n).reshape(n, -1), columns=list('abcd'))
            expected = eval('base{op}df'.format(op=op_str))
            result = eval('m{op}df'.format(op=op_str))
            tm.assert_frame_equal(result, expected)
            if op in ['+', '*']:
                result = getattr(df, op)(m)
                tm.assert_frame_equal(result, expected)
            elif op in ['-', '/']:
                result = getattr(df, rop)(m)
                tm.assert_frame_equal(result, expected)
    df = DataFrame(dict(A=np.random.randn(25000)))
    df.iloc[0:5] = np.nan
    expected = 1 - np.isnan(df.iloc[0:25])
    result = (1 - np.isnan(df)).iloc[0:25]
    tm.assert_frame_equal(result, expected)