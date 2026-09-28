def test_arg_for_errors_in_astype(self):
    s = Series([1, 2, 3])
    msg = "Expected value of kwarg 'errors' to be one of \\['raise', 'ignore'\\]\\. Supplied value is 'False'"
    with pytest.raises(ValueError, match=msg):
        s.astype(np.float64, errors=False)
    s.astype(np.int8, errors='raise')