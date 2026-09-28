def setup_method(self, method):
    dt_data = [pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timestamp('2011-01-03')]
    tz_data = [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-01-02', tz='US/Eastern'), pd.Timestamp('2011-01-03', tz='US/Eastern')]
    td_data = [pd.Timedelta('1 days'), pd.Timedelta('2 days'), pd.Timedelta('3 days')]
    period_data = [pd.Period('2011-01', freq='M'), pd.Period('2011-02', freq='M'), pd.Period('2011-03', freq='M')]
    self.data = {'bool': [True, False, True], 'int64': [1, 2, 3], 'float64': [1.1, np.nan, 3.3], 'category': pd.Categorical(['X', 'Y', 'Z']), 'object': ['a', 'b', 'c'], 'datetime64[ns]': dt_data, 'datetime64[ns, US/Eastern]': tz_data, 'timedelta64[ns]': td_data, 'period[M]': period_data}