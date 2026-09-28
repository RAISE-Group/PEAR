def test_tolerance_tz(self):
    left = pd.DataFrame({'date': pd.date_range(start=pd.to_datetime('2016-01-02'), freq='D', periods=5, tz=pytz.timezone('UTC')), 'value1': np.arange(5)})
    right = pd.DataFrame({'date': pd.date_range(start=pd.to_datetime('2016-01-01'), freq='D', periods=5, tz=pytz.timezone('UTC')), 'value2': list('ABCDE')})
    result = pd.merge_asof(left, right, on='date', tolerance=pd.Timedelta('1 day'))
    expected = pd.DataFrame({'date': pd.date_range(start=pd.to_datetime('2016-01-02'), freq='D', periods=5, tz=pytz.timezone('UTC')), 'value1': np.arange(5), 'value2': list('BCDEE')})
    tm.assert_frame_equal(result, expected)