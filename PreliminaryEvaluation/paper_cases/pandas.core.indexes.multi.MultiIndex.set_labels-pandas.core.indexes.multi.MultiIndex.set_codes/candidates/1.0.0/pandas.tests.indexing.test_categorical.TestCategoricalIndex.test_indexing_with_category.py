def test_indexing_with_category(self):
    cat = DataFrame({'A': ['foo', 'bar', 'baz']})
    exp = DataFrame({'A': [True, False, False]})
    res = cat[['A']] == 'foo'
    tm.assert_frame_equal(res, exp)
    cat['A'] = cat['A'].astype('category')
    res = cat[['A']] == 'foo'
    tm.assert_frame_equal(res, exp)