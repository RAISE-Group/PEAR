def test_to_string_line_width(self):
    df = DataFrame(123, index=range(10, 15), columns=range(30))
    s = df.to_string(line_width=80)
    assert max((len(l) for l in s.split('\n'))) == 80