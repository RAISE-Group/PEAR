def test_loc_getitem_across_dst(self):
    idx = pd.date_range('2017-10-29 01:30:00', tz='Europe/Berlin', periods=5, freq='30 min')
    series2 = pd.Series([0, 1, 2, 3, 4], index=idx)
    t_1 = pd.Timestamp('2017-10-29 02:30:00+02:00', tz='Europe/Berlin', freq='30min')
    t_2 = pd.Timestamp('2017-10-29 02:00:00+01:00', tz='Europe/Berlin', freq='30min')
    result = series2.loc[t_1:t_2]
    expected = pd.Series([2, 3], index=idx[2:4])
    tm.assert_series_equal(result, expected)
    result = series2[t_1]
    expected = 2
    assert result == expected