def test_unicode_name_in_footer(self):
    s = Series([1, 2], name='עברית')
    sf = fmt.SeriesFormatter(s, name='עברית')
    sf._get_footer()