def test_to_string_utf8_columns(self):
    n = 'א'.encode('utf-8')
    with option_context('display.max_rows', 1):
        df = DataFrame([1, 2], columns=[n])
        repr(df)