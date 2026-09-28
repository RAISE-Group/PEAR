def test_period_index_date_overflow(self):
    dates = ['1990-01-01', '2000-01-01', '3005-01-01']
    index = pd.PeriodIndex(dates, freq='D')
    df = pd.DataFrame([4, 5, 6], index=index)
    result = df.to_csv()
    expected_rows = [',0', '1990-01-01,4', '2000-01-01,5', '3005-01-01,6']
    expected = tm.convert_rows_list_to_csv_str(expected_rows)
    assert result == expected
    date_format = '%m-%d-%Y'
    result = df.to_csv(date_format=date_format)
    expected_rows = [',0', '01-01-1990,4', '01-01-2000,5', '01-01-3005,6']
    expected = tm.convert_rows_list_to_csv_str(expected_rows)
    assert result == expected
    dates = ['1990-01-01', pd.NaT, '3005-01-01']
    index = pd.PeriodIndex(dates, freq='D')
    df = pd.DataFrame([4, 5, 6], index=index)
    result = df.to_csv()
    expected_rows = [',0', '1990-01-01,4', ',5', '3005-01-01,6']
    expected = tm.convert_rows_list_to_csv_str(expected_rows)
    assert result == expected