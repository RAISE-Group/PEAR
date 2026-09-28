@pytest.mark.parametrize('tz', tz)
@pytest.mark.parametrize('sort', [None, False])
def test_difference(self, tz, sort):
    rng_dates = ['1/2/2000', '1/3/2000', '1/1/2000', '1/4/2000', '1/5/2000']
    rng1 = pd.DatetimeIndex(rng_dates, tz=tz)
    other1 = pd.date_range('1/6/2000', freq='D', periods=5, tz=tz)
    expected1 = pd.DatetimeIndex(rng_dates, tz=tz)
    rng2 = pd.DatetimeIndex(rng_dates, tz=tz)
    other2 = pd.date_range('1/4/2000', freq='D', periods=5, tz=tz)
    expected2 = pd.DatetimeIndex(rng_dates[:3], tz=tz)
    rng3 = pd.DatetimeIndex(rng_dates, tz=tz)
    other3 = pd.DatetimeIndex([], tz=tz)
    expected3 = pd.DatetimeIndex(rng_dates, tz=tz)
    for rng, other, expected in [(rng1, other1, expected1), (rng2, other2, expected2), (rng3, other3, expected3)]:
        result_diff = rng.difference(other, sort)
        if sort is None:
            expected = expected.sort_values()
        tm.assert_index_equal(result_diff, expected)