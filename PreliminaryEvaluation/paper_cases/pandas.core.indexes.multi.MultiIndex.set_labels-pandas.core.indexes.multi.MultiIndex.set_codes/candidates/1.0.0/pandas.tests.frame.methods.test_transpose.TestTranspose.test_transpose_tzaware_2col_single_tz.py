def test_transpose_tzaware_2col_single_tz(self):
    dti = pd.date_range('2016-04-05 04:30', periods=3, tz='UTC')
    df3 = pd.DataFrame({'A': dti, 'B': dti})
    assert (df3.dtypes == dti.dtype).all()
    res3 = df3.T
    assert (res3.dtypes == dti.dtype).all()