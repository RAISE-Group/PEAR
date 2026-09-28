@pytest.mark.parametrize('op', ['+', '-', '*', '/'])
def test_invalid_type_for_operator_raises(self, parser, engine, op):
    df = DataFrame({'a': [1, 2], 'b': ['c', 'd']})
    msg = "unsupported operand type\\(s\\) for .+: '.+' and '.+'"
    with pytest.raises(TypeError, match=msg):
        df.eval('a {0} b'.format(op), engine=engine, parser=parser)