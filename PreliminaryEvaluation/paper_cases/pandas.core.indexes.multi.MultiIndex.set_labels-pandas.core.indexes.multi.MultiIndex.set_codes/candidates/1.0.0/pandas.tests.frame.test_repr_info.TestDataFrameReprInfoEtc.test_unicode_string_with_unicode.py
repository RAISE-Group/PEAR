def test_unicode_string_with_unicode(self):
    df = DataFrame({'A': ['א']})
    str(df)