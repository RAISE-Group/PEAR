@pytest.mark.parametrize('op', ['__add__', '__sub__', '__mul__'])
def test_arith_flex_frame_mixed(self, op, int_frame, mixed_int_frame, mixed_float_frame):
    f = getattr(operator, op)
    result = getattr(mixed_int_frame, op)(2 + mixed_int_frame)
    expected = f(mixed_int_frame, 2 + mixed_int_frame)
    dtype = None
    if op in ['__sub__']:
        dtype = dict(B='uint64', C=None)
    elif op in ['__add__', '__mul__']:
        dtype = dict(C=None)
    tm.assert_frame_equal(result, expected)
    _check_mixed_int(result, dtype=dtype)
    result = getattr(mixed_float_frame, op)(2 * mixed_float_frame)
    expected = f(mixed_float_frame, 2 * mixed_float_frame)
    tm.assert_frame_equal(result, expected)
    _check_mixed_float(result, dtype=dict(C=None))
    result = getattr(int_frame, op)(2 * int_frame)
    expected = f(int_frame, 2 * int_frame)
    tm.assert_frame_equal(result, expected)