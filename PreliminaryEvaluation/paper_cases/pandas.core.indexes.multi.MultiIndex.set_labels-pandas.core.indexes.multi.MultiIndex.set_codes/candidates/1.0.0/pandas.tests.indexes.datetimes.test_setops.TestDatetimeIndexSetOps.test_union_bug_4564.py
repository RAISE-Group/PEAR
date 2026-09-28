@pytest.mark.parametrize('sort', [None, False])
def test_union_bug_4564(self, sort):
    from pandas import DateOffset
    left = date_range('2013-01-01', '2013-02-01')
    right = left + DateOffset(minutes=15)
    result = left.union(right, sort=sort)
    exp = list(left) + list(right)
    if sort is None:
        exp = DatetimeIndex(sorted(exp))
    else:
        exp = DatetimeIndex(exp)
    tm.assert_index_equal(result, exp)