def test_encode_decode(self):
    base = Series(['a', 'b', 'aä'])
    series = base.str.encode('utf-8')
    f = lambda x: x.decode('utf-8')
    result = series.str.decode('utf-8')
    exp = series.map(f)
    tm.assert_series_equal(result, exp)