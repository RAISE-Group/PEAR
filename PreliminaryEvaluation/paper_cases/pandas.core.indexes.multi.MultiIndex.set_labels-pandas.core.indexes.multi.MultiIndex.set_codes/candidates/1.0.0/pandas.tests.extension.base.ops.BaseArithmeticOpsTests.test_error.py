def test_error(self, data, all_arithmetic_operators):
    op_name = all_arithmetic_operators
    with pytest.raises(AttributeError):
        getattr(data, op_name)