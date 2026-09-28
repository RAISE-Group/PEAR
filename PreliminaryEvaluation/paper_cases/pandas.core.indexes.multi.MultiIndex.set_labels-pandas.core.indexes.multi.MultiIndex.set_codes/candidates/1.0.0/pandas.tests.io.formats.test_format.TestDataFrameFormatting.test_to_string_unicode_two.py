def test_to_string_unicode_two(self):
    dm = DataFrame({'c/σ': []})
    buf = StringIO()
    dm.to_string(buf)