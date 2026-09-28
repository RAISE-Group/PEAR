def test_unicode_string_with_unicode(self):
    df = Series(['א'], name='ב')
    str(df)