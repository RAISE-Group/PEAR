@pytest.mark.parametrize('klass', [Series, DataFrame])
def test_binary_ops_docs(self, klass):
    op_map = {'add': '+', 'sub': '-', 'mul': '*', 'mod': '%', 'pow': '**', 'truediv': '/', 'floordiv': '//'}
    for op_name in op_map:
        operand1 = klass.__name__.lower()
        operand2 = 'other'
        op = op_map[op_name]
        expected_str = ' '.join([operand1, op, operand2])
        assert expected_str in getattr(klass, op_name).__doc__
        expected_str = ' '.join([operand2, op, operand1])
        assert expected_str in getattr(klass, 'r' + op_name).__doc__