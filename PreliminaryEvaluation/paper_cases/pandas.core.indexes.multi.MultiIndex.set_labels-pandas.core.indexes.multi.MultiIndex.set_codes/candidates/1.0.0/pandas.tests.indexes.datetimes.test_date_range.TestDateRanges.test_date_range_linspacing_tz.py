@pytest.mark.parametrize('start,end,result_tz', [['20180101', '20180103', 'US/Eastern'], [datetime(2018, 1, 1), datetime(2018, 1, 3), 'US/Eastern'], [Timestamp('20180101'), Timestamp('20180103'), 'US/Eastern'], [Timestamp('20180101', tz='US/Eastern'), Timestamp('20180103', tz='US/Eastern'), 'US/Eastern'], [Timestamp('20180101', tz='US/Eastern'), Timestamp('20180103', tz='US/Eastern'), None]])
def test_date_range_linspacing_tz(self, start, end, result_tz):
    result = date_range(start, end, periods=3, tz=result_tz)
    expected = date_range('20180101', periods=3, freq='D', tz='US/Eastern')
    tm.assert_index_equal(result, expected)