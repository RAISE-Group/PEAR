@pytest.mark.parametrize('start, end', [[Timestamp(datetime(2014, 3, 6), tz='US/Eastern'), Timestamp(datetime(2014, 3, 12), tz='US/Eastern')], [Timestamp(datetime(2013, 11, 1), tz='US/Eastern'), Timestamp(datetime(2013, 11, 6), tz='US/Eastern')]])
def test_range_tz_dst_straddle_pytz(self, start, end):
    dr = date_range(start, end, freq='D')
    assert dr[0] == start
    assert dr[-1] == end
    assert np.all(dr.hour == 0)
    dr = date_range(start, end, freq='D', tz='US/Eastern')
    assert dr[0] == start
    assert dr[-1] == end
    assert np.all(dr.hour == 0)
    dr = date_range(start.replace(tzinfo=None), end.replace(tzinfo=None), freq='D', tz='US/Eastern')
    assert dr[0] == start
    assert dr[-1] == end
    assert np.all(dr.hour == 0)