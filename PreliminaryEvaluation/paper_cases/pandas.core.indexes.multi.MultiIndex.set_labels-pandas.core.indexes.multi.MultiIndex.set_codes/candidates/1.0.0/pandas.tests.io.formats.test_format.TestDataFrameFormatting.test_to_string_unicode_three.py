def test_to_string_unicode_three(self):
    dm = DataFrame(['Â'])
    buf = StringIO()
    dm.to_string(buf)