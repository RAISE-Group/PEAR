def test_arith_getitem_commute(self):
    df = pd.DataFrame({'A': [1.1, 3.3], 'B': [2.5, -3.9]})

    def _test_op(df, op):
        result = op(df, 1)
        if not df.columns.is_unique:
            raise ValueError('Only unique columns supported by this test')
        for col in result.columns:
            tm.assert_series_equal(result[col], op(df[col], 1))
    _test_op(df, operator.add)
    _test_op(df, operator.sub)
    _test_op(df, operator.mul)
    _test_op(df, operator.truediv)
    _test_op(df, operator.floordiv)
    _test_op(df, operator.pow)
    _test_op(df, lambda x, y: y + x)
    _test_op(df, lambda x, y: y - x)
    _test_op(df, lambda x, y: y * x)
    _test_op(df, lambda x, y: y / x)
    _test_op(df, lambda x, y: y ** x)
    _test_op(df, lambda x, y: x + y)
    _test_op(df, lambda x, y: x - y)
    _test_op(df, lambda x, y: x * y)
    _test_op(df, lambda x, y: x / y)
    _test_op(df, lambda x, y: x ** y)