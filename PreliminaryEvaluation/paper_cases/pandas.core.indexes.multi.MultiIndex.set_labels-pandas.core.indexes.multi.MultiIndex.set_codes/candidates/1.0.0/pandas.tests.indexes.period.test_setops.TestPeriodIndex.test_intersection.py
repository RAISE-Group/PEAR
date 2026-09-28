@pytest.mark.parametrize('sort', [None, False])
def test_intersection(self, sort):
    index = period_range('1/1/2000', '1/20/2000', freq='D')
    result = index[:-5].intersection(index[10:], sort=sort)
    tm.assert_index_equal(result, index[10:-5])
    left = _permute(index[:-5])
    right = _permute(index[10:])
    result = left.intersection(right, sort=sort)
    if sort is None:
        tm.assert_index_equal(result, index[10:-5])
    assert tm.equalContents(result, index[10:-5])
    index = period_range('1/1/2000', '1/20/2000', freq='D')
    index2 = period_range('1/1/2000', '1/20/2000', freq='W-WED')
    with pytest.raises(IncompatibleFrequency):
        index.intersection(index2, sort=sort)
    index3 = period_range('1/1/2000', '1/20/2000', freq='2D')
    with pytest.raises(IncompatibleFrequency):
        index.intersection(index3, sort=sort)