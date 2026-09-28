@pytest.mark.parametrize('other', [0, 1.0, True, 'foo', Timestamp('2017-01-01'), Timestamp('2017-01-01', tz='US/Eastern'), Timedelta('0 days'), Period('2017-01-01', 'D')])
def test_compare_scalar_other(self, op, array, other):
    result = op(array, other)
    expected = self.elementwise_comparison(op, array, other)
    tm.assert_numpy_array_equal(result, expected)