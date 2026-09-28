def _compare_other(self, s, data, op_name, other):
    op = self.get_op_from_name(op_name)
    if op_name == '__eq__':
        assert getattr(data, op_name)(other) is NotImplemented
        assert not op(s, other).all()
    elif op_name == '__ne__':
        assert getattr(data, op_name)(other) is NotImplemented
        assert op(s, other).all()
    else:
        assert getattr(data, op_name)(other) is NotImplemented
        s = pd.Series(data)
        with pytest.raises(TypeError):
            op(s, other)