def test_codes_immutable(self):
    c = Categorical(['a', 'b', 'c', 'a', np.nan])
    exp = np.array([0, 1, 2, 0, -1], dtype='int8')
    tm.assert_numpy_array_equal(c.codes, exp)
    with pytest.raises(ValueError, match='cannot set Categorical codes directly'):
        c.codes = np.array([0, 1, 2, 0, 1], dtype='int8')
    codes = c.codes
    with pytest.raises(ValueError, match='assignment destination is read-only'):
        codes[4] = 1
    c[4] = 'a'
    exp = np.array([0, 1, 2, 0, 0], dtype='int8')
    tm.assert_numpy_array_equal(c.codes, exp)
    c._codes[4] = 2
    exp = np.array([0, 1, 2, 0, 2], dtype='int8')
    tm.assert_numpy_array_equal(c.codes, exp)