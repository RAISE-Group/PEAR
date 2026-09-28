@pytest.mark.parametrize('cache', [True, False])
def test_parsers_dayfirst_yearfirst(self, cache):
    cases = {'10-11-12': [(False, False, datetime(2012, 10, 11)), (True, False, datetime(2012, 11, 10)), (False, True, datetime(2010, 11, 12)), (True, True, datetime(2010, 12, 11))], '20/12/21': [(False, False, datetime(2021, 12, 20)), (True, False, datetime(2021, 12, 20)), (False, True, datetime(2020, 12, 21)), (True, True, datetime(2020, 12, 21))]}
    for date_str, values in cases.items():
        for dayfirst, yearfirst, expected in values:
            dateutil_result = parse(date_str, dayfirst=dayfirst, yearfirst=yearfirst)
            assert dateutil_result == expected
            result1, _, _ = parsing.parse_time_string(date_str, dayfirst=dayfirst, yearfirst=yearfirst)
            if not dayfirst and (not yearfirst):
                result2 = Timestamp(date_str)
                assert result2 == expected
            result3 = to_datetime(date_str, dayfirst=dayfirst, yearfirst=yearfirst, cache=cache)
            result4 = DatetimeIndex([date_str], dayfirst=dayfirst, yearfirst=yearfirst)[0]
            assert result1 == expected
            assert result3 == expected
            assert result4 == expected