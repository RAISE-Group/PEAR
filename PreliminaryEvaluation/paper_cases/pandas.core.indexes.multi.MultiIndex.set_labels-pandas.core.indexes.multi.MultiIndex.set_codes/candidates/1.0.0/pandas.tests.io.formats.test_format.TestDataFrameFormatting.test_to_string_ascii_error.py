def test_to_string_ascii_error(self):
    data = [('0  ', '                        .gitignore ', '     5 ', ' â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢')]
    df = DataFrame(data)
    repr(df)