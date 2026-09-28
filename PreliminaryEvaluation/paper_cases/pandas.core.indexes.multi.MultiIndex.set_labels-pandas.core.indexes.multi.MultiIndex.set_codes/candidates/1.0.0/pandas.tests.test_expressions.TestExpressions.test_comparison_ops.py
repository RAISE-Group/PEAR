@pytest.mark.parametrize('opname,op_str', [('gt', '>'), ('lt', '<'), ('ge', '>='), ('le', '<='), ('eq', '=='), ('ne', '!=')])
@pytest.mark.parametrize('left,right', [(_frame, _frame2), (_mixed, _mixed2)])
def test_comparison_ops(self, opname, op_str, left, right):

    def testit():
        f12 = left + 1
        f22 = right + 1
        op = getattr(operator, opname)
        result = expr._can_use_numexpr(op, op_str, left, f12, 'evaluate')
        assert result != left._is_mixed_type
        result = expr.evaluate(op, op_str, left, f12, use_numexpr=True)
        expected = expr.evaluate(op, op_str, left, f12, use_numexpr=False)
        if isinstance(result, DataFrame):
            tm.assert_frame_equal(result, expected)
        else:
            tm.assert_numpy_array_equal(result, expected.values)
        result = expr._can_use_numexpr(op, op_str, right, f22, 'evaluate')
        assert not result
    expr.set_use_numexpr(False)
    testit()
    expr.set_use_numexpr(True)
    expr.set_numexpr_threads(1)
    testit()
    expr.set_numexpr_threads()
    testit()