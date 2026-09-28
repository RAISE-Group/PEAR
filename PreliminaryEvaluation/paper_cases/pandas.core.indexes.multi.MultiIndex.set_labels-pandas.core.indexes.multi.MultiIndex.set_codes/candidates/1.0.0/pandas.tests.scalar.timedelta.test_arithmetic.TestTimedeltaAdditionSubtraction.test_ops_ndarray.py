def test_ops_ndarray(self):
    td = Timedelta('1 day')
    other = pd.to_timedelta(['1 day']).values
    expected = pd.to_timedelta(['2 days']).values
    tm.assert_numpy_array_equal(td + other, expected)
    tm.assert_numpy_array_equal(other + td, expected)
    msg = "unsupported operand type\\(s\\) for \\+: 'Timedelta' and 'int'"
    with pytest.raises(TypeError, match=msg):
        td + np.array([1])
    msg = "unsupported operand type\\(s\\) for \\+: 'numpy.ndarray' and 'Timedelta'"
    with pytest.raises(TypeError, match=msg):
        np.array([1]) + td
    expected = pd.to_timedelta(['0 days']).values
    tm.assert_numpy_array_equal(td - other, expected)
    tm.assert_numpy_array_equal(-other + td, expected)
    msg = "unsupported operand type\\(s\\) for -: 'Timedelta' and 'int'"
    with pytest.raises(TypeError, match=msg):
        td - np.array([1])
    msg = "unsupported operand type\\(s\\) for -: 'numpy.ndarray' and 'Timedelta'"
    with pytest.raises(TypeError, match=msg):
        np.array([1]) - td
    expected = pd.to_timedelta(['2 days']).values
    tm.assert_numpy_array_equal(td * np.array([2]), expected)
    tm.assert_numpy_array_equal(np.array([2]) * td, expected)
    msg = "ufunc '?multiply'? cannot use operands with types dtype\\('<m8\\[ns\\]'\\) and dtype\\('<m8\\[ns\\]'\\)"
    with pytest.raises(TypeError, match=msg):
        td * other
    with pytest.raises(TypeError, match=msg):
        other * td
    tm.assert_numpy_array_equal(td / other, np.array([1], dtype=np.float64))
    tm.assert_numpy_array_equal(other / td, np.array([1], dtype=np.float64))
    other = pd.to_datetime(['2000-01-01']).values
    expected = pd.to_datetime(['2000-01-02']).values
    tm.assert_numpy_array_equal(td + other, expected)
    tm.assert_numpy_array_equal(other + td, expected)
    expected = pd.to_datetime(['1999-12-31']).values
    tm.assert_numpy_array_equal(-td + other, expected)
    tm.assert_numpy_array_equal(other - td, expected)