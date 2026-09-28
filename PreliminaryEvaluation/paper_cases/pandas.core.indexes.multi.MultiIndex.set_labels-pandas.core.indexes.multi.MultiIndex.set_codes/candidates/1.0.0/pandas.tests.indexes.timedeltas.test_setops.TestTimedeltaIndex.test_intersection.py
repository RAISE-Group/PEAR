@pytest.mark.parametrize('rng, expected', [(timedelta_range('1 day', periods=5, freq='h', name='idx'), timedelta_range('1 day', periods=4, freq='h', name='idx')), (timedelta_range('1 day', periods=5, freq='h', name='other'), timedelta_range('1 day', periods=4, freq='h', name=None)), (timedelta_range('1 day', periods=10, freq='h', name='idx')[5:], TimedeltaIndex([], name='idx'))])
@pytest.mark.parametrize('sort', [None, False])
def test_intersection(self, rng, expected, sort):
    base = timedelta_range('1 day', periods=4, freq='h', name='idx')
    result = base.intersection(rng, sort=sort)
    if sort is None:
        expected = expected.sort_values()
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq