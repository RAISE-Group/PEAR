def test_unstack_fill_frame_categorical(self):
    data = pd.Series(['a', 'b', 'c', 'a'], dtype='category')
    data.index = pd.MultiIndex.from_tuples([('x', 'a'), ('x', 'b'), ('y', 'b'), ('z', 'a')])
    result = data.unstack()
    expected = DataFrame({'a': pd.Categorical(list('axa'), categories=list('abc')), 'b': pd.Categorical(list('bcx'), categories=list('abc'))}, index=list('xyz'))
    tm.assert_frame_equal(result, expected)
    msg = "'fill_value' \\('d'\\) is not in"
    with pytest.raises(TypeError, match=msg):
        data.unstack(fill_value='d')
    result = data.unstack(fill_value='c')
    expected = DataFrame({'a': pd.Categorical(list('aca'), categories=list('abc')), 'b': pd.Categorical(list('bcc'), categories=list('abc'))}, index=list('xyz'))
    tm.assert_frame_equal(result, expected)