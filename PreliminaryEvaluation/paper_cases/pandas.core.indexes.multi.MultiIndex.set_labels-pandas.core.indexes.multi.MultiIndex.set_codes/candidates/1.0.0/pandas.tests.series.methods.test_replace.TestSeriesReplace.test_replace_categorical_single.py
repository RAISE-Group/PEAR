def test_replace_categorical_single(self):
    dti = pd.date_range('2016-01-01', periods=3, tz='US/Pacific')
    s = pd.Series(dti)
    c = s.astype('category')
    expected = c.copy()
    expected = expected.cat.add_categories('foo')
    expected[2] = 'foo'
    expected = expected.cat.remove_unused_categories()
    assert c[2] != 'foo'
    result = c.replace(c[2], 'foo')
    tm.assert_series_equal(expected, result)
    assert c[2] != 'foo'
    c.replace(c[2], 'foo', inplace=True)
    tm.assert_series_equal(expected, c)
    first_value = c[0]
    c.replace(c[1], c[0], inplace=True)
    assert c[0] == c[1] == first_value