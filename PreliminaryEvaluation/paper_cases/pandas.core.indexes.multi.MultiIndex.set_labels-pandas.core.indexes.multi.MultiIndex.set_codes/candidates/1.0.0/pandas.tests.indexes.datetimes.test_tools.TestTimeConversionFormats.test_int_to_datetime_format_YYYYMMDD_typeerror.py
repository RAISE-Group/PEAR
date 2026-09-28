@pytest.mark.parametrize('int_date, expected', [[20121030, datetime(2012, 10, 30)], [199934, datetime(1999, 3, 4)], [2012010101, 2012010101], [20129930, 20129930], [2012993, 2012993], [2121, 2121]])
def test_int_to_datetime_format_YYYYMMDD_typeerror(self, int_date, expected):
    result = to_datetime(int_date, format='%Y%m%d', errors='ignore')
    assert result == expected