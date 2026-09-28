def test_ops_properties(self):
    f = lambda x: isinstance(x, PeriodIndex)
    self.check_ops_properties(PeriodArray._field_ops, f)
    self.check_ops_properties(PeriodArray._object_ops, f)
    self.check_ops_properties(PeriodArray._bool_ops, f)