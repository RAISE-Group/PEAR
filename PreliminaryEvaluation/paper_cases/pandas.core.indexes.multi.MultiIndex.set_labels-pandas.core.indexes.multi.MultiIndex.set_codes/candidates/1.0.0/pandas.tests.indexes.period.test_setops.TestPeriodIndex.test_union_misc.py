@pytest.mark.parametrize('sort', [None, False])
def test_union_misc(self, sort):
    index = period_range('1/1/2000', '1/20/2000', freq='D')
    result = index[:-5].union(index[10:], sort=sort)
    tm.assert_index_equal(result, index)
    result = _permute(index[:-5]).union(_permute(index[10:]), sort=sort)
    if sort is None:
        tm.assert_index_equal(result, index)
    assert tm.equalContents(result, index)
    index = period_range('1/1/2000', '1/20/2000', freq='D')
    index2 = period_range('1/1/2000', '1/20/2000', freq='W-WED')
    with pytest.raises(IncompatibleFrequency):
        index.union(index2, sort=sort)
    index3 = period_range('1/1/2000', '1/20/2000', freq='2D')
    with pytest.raises(IncompatibleFrequency):
        index.join(index3)