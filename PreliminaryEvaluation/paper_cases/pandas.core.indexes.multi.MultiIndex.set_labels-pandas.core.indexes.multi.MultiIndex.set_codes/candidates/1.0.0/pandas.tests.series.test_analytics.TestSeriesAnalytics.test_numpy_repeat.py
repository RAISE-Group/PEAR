def test_numpy_repeat(self):
    s = Series(np.arange(3), name='x')
    expected = Series(s.values.repeat(2), name='x', index=s.index.values.repeat(2))
    tm.assert_series_equal(np.repeat(s, 2), expected)
    msg = "the 'axis' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.repeat(s, 2, axis=0)