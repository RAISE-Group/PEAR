def check_reduce(self, s, op_name, skipna):
    result = getattr(s, op_name)(skipna=skipna)
    expected = getattr(s.astype('float64'), op_name)(skipna=skipna)
    tm.assert_almost_equal(result, expected)