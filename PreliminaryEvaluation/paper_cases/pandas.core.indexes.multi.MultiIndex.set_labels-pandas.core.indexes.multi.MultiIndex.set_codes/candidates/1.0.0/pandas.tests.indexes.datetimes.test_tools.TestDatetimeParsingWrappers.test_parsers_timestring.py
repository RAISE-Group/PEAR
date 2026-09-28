@pytest.mark.parametrize('cache', [True, False])
def test_parsers_timestring(self, cache):
    cases = {'10:15': (parse('10:15'), datetime(1, 1, 1, 10, 15)), '9:05': (parse('9:05'), datetime(1, 1, 1, 9, 5))}
    for date_str, (exp_now, exp_def) in cases.items():
        result1, _, _ = parsing.parse_time_string(date_str)
        result2 = to_datetime(date_str)
        result3 = to_datetime([date_str])
        result4 = Timestamp(date_str)
        result5 = DatetimeIndex([date_str])[0]
        assert result1 == exp_def
        assert result2 == exp_now
        assert result3 == exp_now
        assert result4 == exp_now
        assert result5 == exp_now