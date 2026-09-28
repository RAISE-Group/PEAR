def test_setitem_dtype_upcast(self):
    df = DataFrame([{'a': 1}, {'a': 3, 'b': 2}])
    df['c'] = np.nan
    assert df['c'].dtype == np.float64
    df.loc[0, 'c'] = 'foo'
    expected = DataFrame([{'a': 1, 'b': np.nan, 'c': 'foo'}, {'a': 3, 'b': 2, 'c': np.nan}])
    tm.assert_frame_equal(df, expected)
    df = DataFrame(np.arange(6, dtype='int64').reshape(2, 3), index=list('ab'), columns=['foo', 'bar', 'baz'])
    for val in [3.14, 'wxyz']:
        left = df.copy()
        left.loc['a', 'bar'] = val
        right = DataFrame([[0, val, 2], [3, 4, 5]], index=list('ab'), columns=['foo', 'bar', 'baz'])
        tm.assert_frame_equal(left, right)
        assert is_integer_dtype(left['foo'])
        assert is_integer_dtype(left['baz'])
    left = DataFrame(np.arange(6, dtype='int64').reshape(2, 3) / 10.0, index=list('ab'), columns=['foo', 'bar', 'baz'])
    left.loc['a', 'bar'] = 'wxyz'
    right = DataFrame([[0, 'wxyz', 0.2], [0.3, 0.4, 0.5]], index=list('ab'), columns=['foo', 'bar', 'baz'])
    tm.assert_frame_equal(left, right)
    assert is_float_dtype(left['foo'])
    assert is_float_dtype(left['baz'])