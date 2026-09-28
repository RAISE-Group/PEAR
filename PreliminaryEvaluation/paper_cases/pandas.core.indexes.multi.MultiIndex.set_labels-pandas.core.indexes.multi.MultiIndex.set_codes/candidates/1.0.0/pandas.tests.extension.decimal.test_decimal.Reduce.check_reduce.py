def check_reduce(self, s, op_name, skipna):
    if op_name in ['median', 'skew', 'kurt']:
        with pytest.raises(NotImplementedError):
            getattr(s, op_name)(skipna=skipna)
    else:
        result = getattr(s, op_name)(skipna=skipna)
        expected = getattr(np.asarray(s), op_name)()
        tm.assert_almost_equal(result, expected)