def test_series_partial_set_period(self):
    idx = pd.period_range('2011-01-01', '2011-01-02', freq='D', name='idx')
    ser = Series([0.1, 0.2], index=idx, name='s')
    result = ser.loc[[pd.Period('2011-01-01', freq='D'), pd.Period('2011-01-02', freq='D')]]
    exp = Series([0.1, 0.2], index=idx, name='s')
    tm.assert_series_equal(result, exp, check_index_type=True)
    keys = [pd.Period('2011-01-02', freq='D'), pd.Period('2011-01-02', freq='D'), pd.Period('2011-01-01', freq='D')]
    exp = Series([0.2, 0.2, 0.1], index=pd.PeriodIndex(keys, name='idx'), name='s')
    tm.assert_series_equal(ser.loc[keys], exp, check_index_type=True)
    keys = [pd.Period('2011-01-03', freq='D'), pd.Period('2011-01-02', freq='D'), pd.Period('2011-01-03', freq='D')]
    with pytest.raises(KeyError, match='with any missing labels'):
        ser.loc[keys]