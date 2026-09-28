def check_reduce(self, s, op_name, skipna):
    result = getattr(s, op_name)(skipna=skipna)
    expected = getattr(s.astype('float64'), op_name)(skipna=skipna)
    if np.isnan(expected):
        expected = pd.NA
    elif op_name in ('min', 'max'):
        expected = bool(expected)
    tm.assert_almost_equal(result, expected)