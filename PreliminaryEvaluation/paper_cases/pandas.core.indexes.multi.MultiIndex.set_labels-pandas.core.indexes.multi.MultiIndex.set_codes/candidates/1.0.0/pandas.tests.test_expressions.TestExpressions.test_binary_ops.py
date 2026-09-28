@pytest.mark.parametrize('opname,op_str', [('add', '+'), ('sub', '-'), ('mul', '*'), ('truediv', '/'), ('pow', '**')])
@pytest.mark.parametrize('left,right', [(_frame, _frame2), (_mixed, _mixed2)])
def test_binary_ops(self, opname, op_str, left, right):

    def testit():
        if opname == 'pow':
            return
        op = getattr(operator, opname)
        result = expr._can_use_numexpr(op, op_str, left, left, 'evaluate')
        assert result != left._is_mixed_type
        result = expr.evaluate(op, op_str, left, left, use_numexpr=True)
        expected = expr.evaluate(op, op_str, left, left, use_numexpr=False)
        if isinstance(result, DataFrame):
            tm.assert_frame_equal(result, expected)
        else:
            tm.assert_numpy_array_equal(result, expected.values)
        result = expr._can_use_numexpr(op, op_str, right, right, 'evaluate')
        assert not result
    expr.set_use_numexpr(False)
    testit()
    expr.set_use_numexpr(True)
    expr.set_numexpr_threads(1)
    testit()
    expr.set_numexpr_threads()
    testit()