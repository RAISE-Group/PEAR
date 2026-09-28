@pytest.mark.parametrize('klass', [Index, DatetimeIndex])
def test_constructor_from_series(self, klass):
    expected = DatetimeIndex([Timestamp('20110101'), Timestamp('20120101'), Timestamp('20130101')])
    s = Series([Timestamp('20110101'), Timestamp('20120101'), Timestamp('20130101')])
    result = klass(s)
    tm.assert_index_equal(result, expected)