def test_years_only(self):
    dr = date_range('2014', '2015', freq='M')
    assert dr[0] == datetime(2014, 1, 31)
    assert dr[-1] == datetime(2014, 12, 31)