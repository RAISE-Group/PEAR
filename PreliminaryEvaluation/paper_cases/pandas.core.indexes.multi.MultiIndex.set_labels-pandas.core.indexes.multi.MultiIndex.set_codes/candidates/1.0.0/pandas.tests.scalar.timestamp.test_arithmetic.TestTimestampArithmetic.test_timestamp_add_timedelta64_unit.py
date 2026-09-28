@pytest.mark.parametrize('other,expected_difference', [(np.timedelta64(-123, 'ns'), -123), (np.timedelta64(1234567898, 'ns'), 1234567898), (np.timedelta64(-123, 'us'), -123000), (np.timedelta64(-123, 'ms'), -123000000)])
def test_timestamp_add_timedelta64_unit(self, other, expected_difference):
    ts = Timestamp(datetime.utcnow())
    result = ts + other
    valdiff = result.value - ts.value
    assert valdiff == expected_difference