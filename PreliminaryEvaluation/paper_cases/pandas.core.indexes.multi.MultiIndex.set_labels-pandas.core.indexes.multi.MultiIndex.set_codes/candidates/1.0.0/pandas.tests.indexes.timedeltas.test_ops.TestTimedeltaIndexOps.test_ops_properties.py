def test_ops_properties(self):
    f = lambda x: isinstance(x, TimedeltaIndex)
    self.check_ops_properties(TimedeltaIndex._field_ops, f)
    self.check_ops_properties(TimedeltaIndex._object_ops, f)