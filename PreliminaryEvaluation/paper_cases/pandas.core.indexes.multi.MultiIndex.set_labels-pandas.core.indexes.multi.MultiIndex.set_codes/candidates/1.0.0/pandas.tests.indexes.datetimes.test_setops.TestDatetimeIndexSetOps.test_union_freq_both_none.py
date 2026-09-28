@pytest.mark.parametrize('sort', [None, False])
def test_union_freq_both_none(self, sort):
    expected = bdate_range('20150101', periods=10)
    expected._data.freq = None
    result = expected.union(expected, sort=sort)
    tm.assert_index_equal(result, expected)
    assert result.freq is None