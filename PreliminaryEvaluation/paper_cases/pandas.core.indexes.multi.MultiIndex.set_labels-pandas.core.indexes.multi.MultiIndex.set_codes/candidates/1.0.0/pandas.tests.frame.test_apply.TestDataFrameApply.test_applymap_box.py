def test_applymap_box(self):
    df = pd.DataFrame({'a': [pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02')], 'b': [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-01-02', tz='US/Eastern')], 'c': [pd.Timedelta('1 days'), pd.Timedelta('2 days')], 'd': [pd.Period('2011-01-01', freq='M'), pd.Period('2011-01-02', freq='M')]})
    result = df.applymap(lambda x: type(x).__name__)
    expected = pd.DataFrame({'a': ['Timestamp', 'Timestamp'], 'b': ['Timestamp', 'Timestamp'], 'c': ['Timedelta', 'Timedelta'], 'd': ['Period', 'Period']})
    tm.assert_frame_equal(result, expected)