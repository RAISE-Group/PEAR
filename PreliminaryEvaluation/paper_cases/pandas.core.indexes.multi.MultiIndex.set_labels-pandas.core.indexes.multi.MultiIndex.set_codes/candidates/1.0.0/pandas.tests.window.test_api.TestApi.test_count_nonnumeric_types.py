def test_count_nonnumeric_types(self):
    cols = ['int', 'float', 'string', 'datetime', 'timedelta', 'periods', 'fl_inf', 'fl_nan', 'str_nan', 'dt_nat', 'periods_nat']
    df = DataFrame({'int': [1, 2, 3], 'float': [4.0, 5.0, 6.0], 'string': list('abc'), 'datetime': pd.date_range('20170101', periods=3), 'timedelta': pd.timedelta_range('1 s', periods=3, freq='s'), 'periods': [pd.Period('2012-01'), pd.Period('2012-02'), pd.Period('2012-03')], 'fl_inf': [1.0, 2.0, np.Inf], 'fl_nan': [1.0, 2.0, np.NaN], 'str_nan': ['aa', 'bb', np.NaN], 'dt_nat': [Timestamp('20170101'), Timestamp('20170203'), Timestamp(None)], 'periods_nat': [pd.Period('2012-01'), pd.Period('2012-02'), pd.Period(None)]}, columns=cols)
    expected = DataFrame({'int': [1.0, 2.0, 2.0], 'float': [1.0, 2.0, 2.0], 'string': [1.0, 2.0, 2.0], 'datetime': [1.0, 2.0, 2.0], 'timedelta': [1.0, 2.0, 2.0], 'periods': [1.0, 2.0, 2.0], 'fl_inf': [1.0, 2.0, 2.0], 'fl_nan': [1.0, 2.0, 1.0], 'str_nan': [1.0, 2.0, 1.0], 'dt_nat': [1.0, 2.0, 1.0], 'periods_nat': [1.0, 2.0, 1.0]}, columns=cols)
    result = df.rolling(window=2, min_periods=0).count()
    tm.assert_frame_equal(result, expected)
    result = df.rolling(1, min_periods=0).count()
    expected = df.notna().astype(float)
    tm.assert_frame_equal(result, expected)