def test_datetimelike_frame(self):
    df = DataFrame({'date': [pd.Timestamp('20130101').tz_localize('UTC')] + [pd.NaT] * 5})
    with option_context('display.max_rows', 5):
        result = str(df)
        assert '2013-01-01 00:00:00+00:00' in result
        assert 'NaT' in result
        assert '...' in result
        assert '[6 rows x 1 columns]' in result
    dts = [pd.Timestamp('2011-01-01', tz='US/Eastern')] * 5 + [pd.NaT] * 5
    df = pd.DataFrame({'dt': dts, 'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    with option_context('display.max_rows', 5):
        expected = '                          dt   x\n0  2011-01-01 00:00:00-05:00   1\n1  2011-01-01 00:00:00-05:00   2\n..                       ...  ..\n8                        NaT   9\n9                        NaT  10\n\n[10 rows x 2 columns]'
        assert repr(df) == expected
    dts = [pd.NaT] * 5 + [pd.Timestamp('2011-01-01', tz='US/Eastern')] * 5
    df = pd.DataFrame({'dt': dts, 'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    with option_context('display.max_rows', 5):
        expected = '                          dt   x\n0                        NaT   1\n1                        NaT   2\n..                       ...  ..\n8  2011-01-01 00:00:00-05:00   9\n9  2011-01-01 00:00:00-05:00  10\n\n[10 rows x 2 columns]'
        assert repr(df) == expected
    dts = [pd.Timestamp('2011-01-01', tz='Asia/Tokyo')] * 5 + [pd.Timestamp('2011-01-01', tz='US/Eastern')] * 5
    df = pd.DataFrame({'dt': dts, 'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    with option_context('display.max_rows', 5):
        expected = '                           dt   x\n0   2011-01-01 00:00:00+09:00   1\n1   2011-01-01 00:00:00+09:00   2\n..                        ...  ..\n8   2011-01-01 00:00:00-05:00   9\n9   2011-01-01 00:00:00-05:00  10\n\n[10 rows x 2 columns]'
        assert repr(df) == expected