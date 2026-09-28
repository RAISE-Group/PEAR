@pytest.mark.parametrize('opname', ['add', 'sub', 'mul', 'truediv', 'floordiv'])
def test_op(self, opname):
    sparse_op = getattr(splib, f'sparse_{opname}_float64')
    python_op = getattr(operator, opname)
    self._op_tests(sparse_op, python_op)