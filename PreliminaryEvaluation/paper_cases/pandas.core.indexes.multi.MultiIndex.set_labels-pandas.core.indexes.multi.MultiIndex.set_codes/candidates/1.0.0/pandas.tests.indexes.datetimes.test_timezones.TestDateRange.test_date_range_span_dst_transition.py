@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_date_range_span_dst_transition(self, tzstr):
    dr = date_range('03/06/2012 00:00', periods=200, freq='W-FRI', tz='US/Eastern')
    assert (dr.hour == 0).all()
    dr = date_range('2012-11-02', periods=10, tz=tzstr)
    result = dr.hour
    expected = Index([0] * 10)
    tm.assert_index_equal(result, expected)