@pytest.mark.parametrize('other', [(Interval(0, 1), Interval(Timedelta('1 day'), Timedelta('2 days')), Interval(4, 5, 'both'), Interval(10, 20, 'neither')), (0, 1.5, Timestamp('20170103'), np.nan), (Timestamp('20170102', tz='US/Eastern'), Timedelta('2 days'), 'baz', pd.NaT)])
def test_compare_list_like_object(self, op, array, other):
    result = op(array, other)
    expected = self.elementwise_comparison(op, array, other)
    tm.assert_numpy_array_equal(result, expected)