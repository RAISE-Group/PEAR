def test_mixed(self):
    x = Series([datetime(2013, 1, 1), datetime(2013, 1, 1, 12), pd.NaT])
    result = fmt.Datetime64Formatter(x).get_result()
    assert result[0].strip() == '2013-01-01 00:00:00'
    assert result[1].strip() == '2013-01-01 12:00:00'