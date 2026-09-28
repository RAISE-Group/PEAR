def test_to_csv_quote_none(self):
    df = DataFrame({'A': ['hello', '{"hello"}']})
    for encoding in (None, 'utf-8'):
        buf = StringIO()
        df.to_csv(buf, quoting=csv.QUOTE_NONE, encoding=encoding, index=False)
        result = buf.getvalue()
        expected_rows = ['A', 'hello', '{"hello"}']
        expected = tm.convert_rows_list_to_csv_str(expected_rows)
        assert result == expected