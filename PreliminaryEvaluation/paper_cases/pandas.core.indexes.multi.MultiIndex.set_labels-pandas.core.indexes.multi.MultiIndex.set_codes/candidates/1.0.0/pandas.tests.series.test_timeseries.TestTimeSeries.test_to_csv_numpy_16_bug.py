def test_to_csv_numpy_16_bug(self):
    frame = DataFrame({'a': date_range('1/1/2000', periods=10)})
    buf = StringIO()
    frame.to_csv(buf)
    result = buf.getvalue()
    assert '2000-01-01' in result