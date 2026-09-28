@pytest.mark.parametrize('maybe_int', [True, False])
@pytest.mark.parametrize('infinity', ['inf', 'inF', 'iNf', 'Inf', 'iNF', 'InF', 'INf', 'INF'])
def test_maybe_convert_numeric_infinities(self, infinity, maybe_int):
    na_values = {'', 'NULL', 'nan'}
    pos = np.array(['inf'], dtype=np.float64)
    neg = np.array(['-inf'], dtype=np.float64)
    msg = 'Unable to parse string'
    out = lib.maybe_convert_numeric(np.array([infinity], dtype=object), na_values, maybe_int)
    tm.assert_numpy_array_equal(out, pos)
    out = lib.maybe_convert_numeric(np.array(['-' + infinity], dtype=object), na_values, maybe_int)
    tm.assert_numpy_array_equal(out, neg)
    out = lib.maybe_convert_numeric(np.array([infinity], dtype=object), na_values, maybe_int)
    tm.assert_numpy_array_equal(out, pos)
    out = lib.maybe_convert_numeric(np.array(['+' + infinity], dtype=object), na_values, maybe_int)
    tm.assert_numpy_array_equal(out, pos)
    with pytest.raises(ValueError, match=msg):
        lib.maybe_convert_numeric(np.array(['foo_' + infinity], dtype=object), na_values, maybe_int)