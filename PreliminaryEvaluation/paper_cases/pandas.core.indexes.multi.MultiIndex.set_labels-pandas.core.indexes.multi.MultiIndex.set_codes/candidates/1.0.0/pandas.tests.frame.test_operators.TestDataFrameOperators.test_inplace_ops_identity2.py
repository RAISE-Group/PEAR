@pytest.mark.parametrize('op', ['add', 'and', 'div', 'floordiv', 'mod', 'mul', 'or', 'pow', 'sub', 'truediv', 'xor'])
def test_inplace_ops_identity2(self, op):
    if op == 'div':
        return
    df = DataFrame({'a': [1.0, 2.0, 3.0], 'b': [1, 2, 3]})
    operand = 2
    if op in ('and', 'or', 'xor'):
        df['a'] = [True, False, True]
    df_copy = df.copy()
    iop = '__i{}__'.format(op)
    op = '__{}__'.format(op)
    getattr(df, iop)(operand)
    expected = getattr(df_copy, op)(operand)
    tm.assert_frame_equal(df, expected)
    expected = id(df)
    assert id(df) == expected