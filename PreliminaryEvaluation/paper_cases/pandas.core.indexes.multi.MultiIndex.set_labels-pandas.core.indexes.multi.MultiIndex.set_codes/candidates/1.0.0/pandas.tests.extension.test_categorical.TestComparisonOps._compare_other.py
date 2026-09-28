def _compare_other(self, s, data, op_name, other):
    op = self.get_op_from_name(op_name)
    if op_name == '__eq__':
        result = op(s, other)
        expected = s.combine(other, lambda x, y: x == y)
        assert (result == expected).all()
    elif op_name == '__ne__':
        result = op(s, other)
        expected = s.combine(other, lambda x, y: x != y)
        assert (result == expected).all()
    else:
        with pytest.raises(TypeError):
            op(data, other)