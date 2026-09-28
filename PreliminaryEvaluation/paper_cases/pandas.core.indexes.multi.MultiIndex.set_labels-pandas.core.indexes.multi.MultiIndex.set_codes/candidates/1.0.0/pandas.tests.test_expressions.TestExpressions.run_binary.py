def run_binary(self, df, other):
    """
        tests solely that the result is the same whether or not numexpr is
        enabled.  Need to test whether the function does the correct thing
        elsewhere.
        """
    expr._MIN_ELEMENTS = 0
    expr.set_test_mode(True)
    operations = ['gt', 'lt', 'ge', 'le', 'eq', 'ne']
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
            expr.get_test_result()
            result = op(df, other)
            used_numexpr = expr.get_test_result()
            assert used_numexpr, 'Did not use numexpr as expected.'
            tm.assert_equal(expected, result)