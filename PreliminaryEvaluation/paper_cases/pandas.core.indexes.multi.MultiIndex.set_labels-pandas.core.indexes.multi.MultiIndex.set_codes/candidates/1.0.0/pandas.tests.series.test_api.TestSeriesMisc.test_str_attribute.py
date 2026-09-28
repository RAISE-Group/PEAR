def test_str_attribute(self):
    methods = ['strip', 'rstrip', 'lstrip']
    s = Series([' jack', 'jill ', ' jesse ', 'frank'])
    for method in methods:
        expected = Series([getattr(str, method)(x) for x in s.values])
        tm.assert_series_equal(getattr(Series.str, method)(s.str), expected)
    s = Series(range(5))
    with pytest.raises(AttributeError, match='only use .str accessor'):
        s.str.repeat(2)