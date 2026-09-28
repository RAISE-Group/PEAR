def test_transpose_object_to_tzaware_mixed_tz(self):
    dti = pd.date_range('2016-04-05 04:30', periods=3, tz='UTC')
    dti2 = dti.tz_convert('US/Pacific')
    df2 = pd.DataFrame([dti, dti2])
    assert (df2.dtypes == object).all()
    res2 = df2.T
    assert (res2.dtypes == [dti.dtype, dti2.dtype]).all()