def test_transpose_tzaware_2col_mixed_tz(self):
    dti = pd.date_range('2016-04-05 04:30', periods=3, tz='UTC')
    dti2 = dti.tz_convert('US/Pacific')
    df4 = pd.DataFrame({'A': dti, 'B': dti2})
    assert (df4.dtypes == [dti.dtype, dti2.dtype]).all()
    assert (df4.T.dtypes == object).all()
    tm.assert_frame_equal(df4.T.T, df4)