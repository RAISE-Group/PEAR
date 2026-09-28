@pytest.mark.parametrize('other', [np.arange(4, dtype='int64'), np.arange(4, dtype='float64'), date_range('2017-01-01', periods=4), date_range('2017-01-01', periods=4, tz='US/Eastern'), timedelta_range('0 days', periods=4), period_range('2017-01-01', periods=4, freq='D'), Categorical(list('abab')), Categorical(date_range('2017-01-01', periods=4)), pd.array(list('abcd')), pd.array(['foo', 3.14, None, object()])], ids=lambda x: str(x.dtype))
def test_compare_list_like_other(self, op, array, other):
    result = op(array, other)
    expected = self.elementwise_comparison(op, array, other)
    tm.assert_numpy_array_equal(result, expected)