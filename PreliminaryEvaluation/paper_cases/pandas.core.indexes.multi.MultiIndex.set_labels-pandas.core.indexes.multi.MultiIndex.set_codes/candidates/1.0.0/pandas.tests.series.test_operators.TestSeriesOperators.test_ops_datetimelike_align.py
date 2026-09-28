def test_ops_datetimelike_align(self):
    dt = Series(date_range('2012-1-1', periods=3, freq='D'))
    dt.iloc[2] = np.nan
    dt2 = dt[::-1]
    expected = Series([timedelta(0), timedelta(0), pd.NaT])
    result = dt2 - dt
    tm.assert_series_equal(result, expected)
    expected = Series(expected, name=0)
    result = (dt2.to_frame() - dt.to_frame())[0]
    tm.assert_series_equal(result, expected)