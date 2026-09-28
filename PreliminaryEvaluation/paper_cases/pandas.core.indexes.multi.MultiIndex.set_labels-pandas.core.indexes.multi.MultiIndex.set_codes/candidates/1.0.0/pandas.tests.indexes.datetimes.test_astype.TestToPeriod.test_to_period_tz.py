@pytest.mark.parametrize('tz', ['US/Eastern', pytz.utc, tzlocal(), 'dateutil/US/Eastern', dateutil.tz.tzutc()])
def test_to_period_tz(self, tz):
    ts = date_range('1/1/2000', '2/1/2000', tz=tz)
    with tm.assert_produces_warning(UserWarning):
        result = ts.to_period()[0]
        expected = ts[0].to_period()
    assert result == expected
    expected = date_range('1/1/2000', '2/1/2000').to_period()
    with tm.assert_produces_warning(UserWarning):
        result = ts.to_period()
    tm.assert_index_equal(result, expected)