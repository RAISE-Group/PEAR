@pytest.mark.parametrize('nan', [np.nan, np.float64('NaN'), float('nan')])
def test_td_div_nan(self, nan):
    td = Timedelta(10, unit='d')
    result = td / nan
    assert result is NaT
    result = td // nan
    assert result is NaT