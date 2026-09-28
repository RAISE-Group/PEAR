def test_ops_properties(self):
    f = lambda x: isinstance(x, DatetimeIndex)
    self.check_ops_properties(DatetimeIndex._field_ops, f)
    self.check_ops_properties(DatetimeIndex._object_ops, f)
    self.check_ops_properties(DatetimeIndex._bool_ops, f)