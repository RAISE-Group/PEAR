def test_construction_with_conversions(self):
    arr = np.array([1, 2, 3], dtype='timedelta64[s]')
    df = DataFrame(index=range(3))
    df['A'] = arr
    expected = DataFrame({'A': pd.timedelta_range('00:00:01', periods=3, freq='s')}, index=range(3))
    tm.assert_frame_equal(df, expected)
    expected = DataFrame({'dt1': Timestamp('20130101'), 'dt2': date_range('20130101', periods=3)}, index=range(3))
    df = DataFrame(index=range(3))
    df['dt1'] = np.datetime64('2013-01-01')
    df['dt2'] = np.array(['2013-01-01', '2013-01-02', '2013-01-03'], dtype='datetime64[D]')
    tm.assert_frame_equal(df, expected)