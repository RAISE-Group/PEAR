def test_to_string_index_formatter(self):
    df = DataFrame([range(5), range(5, 10), range(10, 15)])
    rs = df.to_string(formatters={'__index__': lambda x: 'abc'[x]})
    xp = '    0   1   2   3   4\na   0   1   2   3   4\nb   5   6   7   8   9\nc  10  11  12  13  14'
    assert rs == xp