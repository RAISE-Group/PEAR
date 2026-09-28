@pytest.mark.parametrize('left, right', [(0, 1), (Timedelta('0 days'), Timedelta('1 day')), (Timestamp('2018-01-01'), Timestamp('2018-01-02')), (Timestamp('2018-01-01', tz='US/Eastern'), Timestamp('2018-01-02', tz='US/Eastern'))])
def test_is_empty(self, left, right, closed):
    iv = Interval(left, right, closed)
    assert iv.is_empty is False
    iv = Interval(left, left, closed)
    result = iv.is_empty
    expected = closed != 'both'
    assert result is expected