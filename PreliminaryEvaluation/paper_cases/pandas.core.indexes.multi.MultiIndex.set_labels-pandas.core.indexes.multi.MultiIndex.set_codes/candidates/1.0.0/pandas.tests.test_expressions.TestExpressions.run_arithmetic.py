def run_arithmetic(self, df, other):
    expr._MIN_ELEMENTS = 0
    operations = ['add', 'sub', 'mul', 'mod', 'truediv', 'floordiv']
    for test_flex in [True, False]:
        for arith in operations:
            if test_flex:
                op = lambda x, y: getattr(x, arith)(y)
                op.__name__ = arith
            else:
                op = getattr(operator, arith)
            expr.set_use_numexpr(False)
            expected = op(df, other)
            expr.set_use_numexpr(True)
            result = op(df, other)
            if arith == 'truediv':
                if expected.ndim == 1:
                    assert expected.dtype.kind == 'f'
                else:
                    assert all((x.kind == 'f' for x in expected.dtypes.values))
            tm.assert_equal(expected, result)