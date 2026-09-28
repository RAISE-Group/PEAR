def test_map_with_string_constructor(self):
    raw = [2005, 2007, 2009]
    index = PeriodIndex(raw, freq='A')
    expected = Index([str(num) for num in raw])
    res = index.map(str)
    assert isinstance(res, Index)
    assert all((isinstance(resi, str) for resi in res))
    tm.assert_index_equal(res, expected)