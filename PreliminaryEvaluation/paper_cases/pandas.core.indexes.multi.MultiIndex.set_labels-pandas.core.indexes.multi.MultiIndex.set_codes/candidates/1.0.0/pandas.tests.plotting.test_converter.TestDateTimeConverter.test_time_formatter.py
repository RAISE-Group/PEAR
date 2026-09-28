@pytest.mark.parametrize('time,format_expected', [(0, '00:00'), (86399.999999, '23:59:59.999999'), (90000, '01:00'), (3723, '01:02:03'), (39723.2, '11:02:03.200')])
def test_time_formatter(self, time, format_expected):
    result = self.tc(time)
    assert result == format_expected