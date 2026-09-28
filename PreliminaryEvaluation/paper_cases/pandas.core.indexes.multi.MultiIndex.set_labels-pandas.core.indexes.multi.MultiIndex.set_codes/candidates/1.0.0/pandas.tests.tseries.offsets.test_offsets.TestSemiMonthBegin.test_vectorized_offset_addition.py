@pytest.mark.parametrize('klass', [Series, DatetimeIndex])
def test_vectorized_offset_addition(self, klass):
    s = klass([Timestamp('2000-01-15 00:15:00', tz='US/Central'), Timestamp('2000-02-15', tz='US/Central')], name='a')
    with tm.assert_produces_warning(None):
        result = s + SemiMonthBegin()
        result2 = SemiMonthBegin() + s
    exp = klass([Timestamp('2000-02-01 00:15:00', tz='US/Central'), Timestamp('2000-03-01', tz='US/Central')], name='a')
    tm.assert_equal(result, exp)
    tm.assert_equal(result2, exp)
    s = klass([Timestamp('2000-01-01 00:15:00', tz='US/Central'), Timestamp('2000-02-01', tz='US/Central')], name='a')
    with tm.assert_produces_warning(None):
        result = s + SemiMonthBegin()
        result2 = SemiMonthBegin() + s
    exp = klass([Timestamp('2000-01-15 00:15:00', tz='US/Central'), Timestamp('2000-02-15', tz='US/Central')], name='a')
    tm.assert_equal(result, exp)
    tm.assert_equal(result2, exp)