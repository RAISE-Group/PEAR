@pytest.mark.parametrize('periods, freq', [(3, '2D'), (5, 'D'), (6, '19H12T'), (7, '16H'), (9, '12H')])
def test_linspace_behavior(self, periods, freq):
    result = timedelta_range(start='0 days', end='4 days', periods=periods)
    expected = timedelta_range(start='0 days', end='4 days', freq=freq)
    tm.assert_index_equal(result, expected)