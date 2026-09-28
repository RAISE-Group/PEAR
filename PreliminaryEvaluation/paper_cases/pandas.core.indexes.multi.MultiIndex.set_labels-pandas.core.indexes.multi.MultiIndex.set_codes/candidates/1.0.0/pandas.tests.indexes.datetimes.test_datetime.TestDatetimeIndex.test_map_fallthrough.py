def test_map_fallthrough(self, capsys):
    dti = date_range('2017-01-01', '2018-01-01', freq='B')
    dti.map(lambda x: pd.Period(year=x.year, month=x.month, freq='M'))
    captured = capsys.readouterr()
    assert captured.err == ''