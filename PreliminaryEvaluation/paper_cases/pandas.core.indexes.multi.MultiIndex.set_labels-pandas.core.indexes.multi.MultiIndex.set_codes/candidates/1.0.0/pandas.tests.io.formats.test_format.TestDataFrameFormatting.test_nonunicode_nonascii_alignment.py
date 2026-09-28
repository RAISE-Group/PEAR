def test_nonunicode_nonascii_alignment(self):
    df = DataFrame([['aaÃ¤Ã¤', 1], ['bbbb', 2]])
    rep_str = df.to_string()
    lines = rep_str.split('\n')
    assert len(lines[1]) == len(lines[2])