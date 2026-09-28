@pytest.mark.parametrize('attr', ['makeDateIndex', 'makePeriodIndex', 'makeTimedeltaIndex'])
def test_map_tseries_indices_return_index(self, attr):
    index = getattr(tm, attr)(10)
    expected = Index([1] * 10)
    result = index.map(lambda x: 1)
    tm.assert_index_equal(expected, result)