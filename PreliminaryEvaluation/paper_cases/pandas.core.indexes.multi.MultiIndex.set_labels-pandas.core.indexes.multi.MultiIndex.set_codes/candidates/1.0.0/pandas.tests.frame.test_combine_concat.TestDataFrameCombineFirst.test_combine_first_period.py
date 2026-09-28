def test_combine_first_period(self):
    data1 = pd.PeriodIndex(['2011-01', 'NaT', '2011-03', '2011-04'], freq='M')
    df1 = pd.DataFrame({'P': data1}, index=[1, 3, 5, 7])
    data2 = pd.PeriodIndex(['2012-01-01', '2012-02', '2012-03'], freq='M')
    df2 = pd.DataFrame({'P': data2}, index=[2, 4, 5])
    res = df1.combine_first(df2)
    exp_dts = pd.PeriodIndex(['2011-01', '2012-01', 'NaT', '2012-02', '2011-03', '2011-04'], freq='M')
    exp = pd.DataFrame({'P': exp_dts}, index=[1, 2, 3, 4, 5, 7])
    tm.assert_frame_equal(res, exp)
    assert res['P'].dtype == data1.dtype
    dts2 = pd.PeriodIndex(['2012-01-01', '2012-01-02', '2012-01-03'], freq='D')
    df2 = pd.DataFrame({'P': dts2}, index=[2, 4, 5])
    res = df1.combine_first(df2)
    exp_dts = [pd.Period('2011-01', freq='M'), pd.Period('2012-01-01', freq='D'), pd.NaT, pd.Period('2012-01-02', freq='D'), pd.Period('2011-03', freq='M'), pd.Period('2011-04', freq='M')]
    exp = pd.DataFrame({'P': exp_dts}, index=[1, 2, 3, 4, 5, 7])
    tm.assert_frame_equal(res, exp)
    assert res['P'].dtype == 'object'