@pytest.mark.parametrize('tz', tz)
@pytest.mark.parametrize('sort', [None, False])
def test_union(self, tz, sort):
    rng1 = pd.date_range('1/1/2000', freq='D', periods=5, tz=tz)
    other1 = pd.date_range('1/6/2000', freq='D', periods=5, tz=tz)
    expected1 = pd.date_range('1/1/2000', freq='D', periods=10, tz=tz)
    expected1_notsorted = pd.DatetimeIndex(list(other1) + list(rng1))
    rng2 = pd.date_range('1/1/2000', freq='D', periods=5, tz=tz)
    other2 = pd.date_range('1/4/2000', freq='D', periods=5, tz=tz)
    expected2 = pd.date_range('1/1/2000', freq='D', periods=8, tz=tz)
    expected2_notsorted = pd.DatetimeIndex(list(other2) + list(rng2[:3]))
    rng3 = pd.date_range('1/1/2000', freq='D', periods=5, tz=tz)
    other3 = pd.DatetimeIndex([], tz=tz)
    expected3 = pd.date_range('1/1/2000', freq='D', periods=5, tz=tz)
    expected3_notsorted = rng3
    for rng, other, exp, exp_notsorted in [(rng1, other1, expected1, expected1_notsorted), (rng2, other2, expected2, expected2_notsorted), (rng3, other3, expected3, expected3_notsorted)]:
        result_union = rng.union(other, sort=sort)
        tm.assert_index_equal(result_union, exp)
        result_union = other.union(rng, sort=sort)
        if sort is None:
            tm.assert_index_equal(result_union, exp)
        else:
            tm.assert_index_equal(result_union, exp_notsorted)