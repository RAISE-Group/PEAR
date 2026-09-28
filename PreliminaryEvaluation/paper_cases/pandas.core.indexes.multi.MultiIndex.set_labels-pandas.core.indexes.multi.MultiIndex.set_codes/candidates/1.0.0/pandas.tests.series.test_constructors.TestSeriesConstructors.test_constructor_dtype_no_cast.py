def test_constructor_dtype_no_cast(self):
    s = Series([1, 2, 3])
    s2 = Series(s, dtype=np.int64)
    s2[1] = 5
    assert s[1] == 5