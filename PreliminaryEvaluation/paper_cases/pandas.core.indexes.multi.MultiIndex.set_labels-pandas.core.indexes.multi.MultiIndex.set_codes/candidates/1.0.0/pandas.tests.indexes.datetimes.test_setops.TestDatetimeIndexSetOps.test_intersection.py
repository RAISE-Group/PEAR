@pytest.mark.parametrize('tz', [None, 'Asia/Tokyo', 'US/Eastern', 'dateutil/US/Pacific'])
@pytest.mark.parametrize('sort', [None, False])
def test_intersection(self, tz, sort):
    base = date_range('6/1/2000', '6/30/2000', freq='D', name='idx')
    rng2 = date_range('5/15/2000', '6/20/2000', freq='D', name='idx')
    expected2 = date_range('6/1/2000', '6/20/2000', freq='D', name='idx')
    rng3 = date_range('5/15/2000', '6/20/2000', freq='D', name='other')
    expected3 = date_range('6/1/2000', '6/20/2000', freq='D', name=None)
    rng4 = date_range('7/1/2000', '7/31/2000', freq='D', name='idx')
    expected4 = DatetimeIndex([], name='idx')
    for rng, expected in [(rng2, expected2), (rng3, expected3), (rng4, expected4)]:
        result = base.intersection(rng)
        tm.assert_index_equal(result, expected)
        assert result.name == expected.name
        assert result.freq == expected.freq
        assert result.tz == expected.tz
    base = DatetimeIndex(['2011-01-05', '2011-01-04', '2011-01-02', '2011-01-03'], tz=tz, name='idx')
    rng2 = DatetimeIndex(['2011-01-04', '2011-01-02', '2011-02-02', '2011-02-03'], tz=tz, name='idx')
    expected2 = DatetimeIndex(['2011-01-04', '2011-01-02'], tz=tz, name='idx')
    rng3 = DatetimeIndex(['2011-01-04', '2011-01-02', '2011-02-02', '2011-02-03'], tz=tz, name='other')
    expected3 = DatetimeIndex(['2011-01-04', '2011-01-02'], tz=tz, name=None)
    rng4 = date_range('7/1/2000', '7/31/2000', freq='D', tz=tz, name='idx')
    expected4 = DatetimeIndex([], tz=tz, name='idx')
    for rng, expected in [(rng2, expected2), (rng3, expected3), (rng4, expected4)]:
        result = base.intersection(rng, sort=sort)
        if sort is None:
            expected = expected.sort_values()
        tm.assert_index_equal(result, expected)
        assert result.name == expected.name
        assert result.freq is None
        assert result.tz == expected.tz