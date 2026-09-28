def test_api(self):
    assert Series.str is strings.StringMethods
    assert isinstance(Series(['']).str, strings.StringMethods)