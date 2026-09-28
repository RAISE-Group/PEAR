def test_scalar_na_logical_ops_corners(self):
    s = Series([2, 3, 4, 5, 6, 7, 8, 9, 10])
    with pytest.raises(TypeError):
        s & datetime(2005, 1, 1)
    s = Series([2, 3, 4, 5, 6, 7, 8, 9, datetime(2005, 1, 1)])
    s[::2] = np.nan
    expected = Series(True, index=s.index)
    expected[::2] = False
    result = s & list(s)
    tm.assert_series_equal(result, expected)
    d = DataFrame({'A': s})
    with pytest.raises(TypeError):
        d.__and__(s, axis='columns')
    with pytest.raises(TypeError):
        d.__and__(s, axis=1)
    with pytest.raises(TypeError):
        s & d
    with pytest.raises(TypeError):
        d & s
    expected = (s & s).to_frame('A')
    result = d.__and__(s, axis='index')
    tm.assert_frame_equal(result, expected)
    result = d.__and__(s, axis=0)
    tm.assert_frame_equal(result, expected)