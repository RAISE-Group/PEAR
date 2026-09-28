def test_constructor_categorical(self):
    df = DataFrame({'A': list('abc')}, dtype='category')
    expected = Series(list('abc'), dtype='category', name='A')
    tm.assert_series_equal(df['A'], expected)
    s = Series(list('abc'), dtype='category')
    result = s.to_frame()
    expected = Series(list('abc'), dtype='category', name=0)
    tm.assert_series_equal(result[0], expected)
    result = s.to_frame(name='foo')
    expected = Series(list('abc'), dtype='category', name='foo')
    tm.assert_series_equal(result['foo'], expected)
    df = DataFrame(list('abc'), dtype='category')
    expected = Series(list('abc'), dtype='category', name=0)
    tm.assert_series_equal(df[0], expected)
    df = DataFrame([Categorical(list('abc'))])
    expected = DataFrame({0: Series(list('abc'), dtype='category')})
    tm.assert_frame_equal(df, expected)
    df = DataFrame([Categorical(list('abc')), Categorical(list('abd'))])
    expected = DataFrame({0: Series(list('abc'), dtype='category'), 1: Series(list('abd'), dtype='category')}, columns=[0, 1])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([Categorical(list('abc')), list('def')])
    expected = DataFrame({0: Series(list('abc'), dtype='category'), 1: list('def')}, columns=[0, 1])
    tm.assert_frame_equal(df, expected)
    msg = 'Shape of passed values is \\(6, 2\\), indices imply \\(3, 2\\)'
    with pytest.raises(ValueError, match=msg):
        DataFrame([Categorical(list('abc')), Categorical(list('abdefg'))])
    msg = '> 1 ndim Categorical are not supported at this time'
    with pytest.raises(NotImplementedError, match=msg):
        Categorical(np.array([list('abcd')]))