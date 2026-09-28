def test_constructor_Series_named(self):
    a = Series([1, 2, 3], index=['a', 'b', 'c'], name='x')
    df = DataFrame(a)
    assert df.columns[0] == 'x'
    tm.assert_index_equal(df.index, a.index)
    arr = np.random.randn(10)
    s = Series(arr, name='x')
    df = DataFrame(s)
    expected = DataFrame(dict(x=s))
    tm.assert_frame_equal(df, expected)
    s = Series(arr, index=range(3, 13))
    df = DataFrame(s)
    expected = DataFrame({0: s})
    tm.assert_frame_equal(df, expected)
    msg = 'Shape of passed values is \\(10, 1\\), indices imply \\(10, 2\\)'
    with pytest.raises(ValueError, match=msg):
        DataFrame(s, columns=[1, 2])
    a = Series([], name='x', dtype=object)
    df = DataFrame(a)
    assert df.columns[0] == 'x'
    s1 = Series(arr, name='x')
    df = DataFrame([s1, arr]).T
    expected = DataFrame({'x': s1, 'Unnamed 0': arr}, columns=['x', 'Unnamed 0'])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([arr, s1]).T
    expected = DataFrame({1: s1, 0: arr}, columns=[0, 1])
    tm.assert_frame_equal(df, expected)