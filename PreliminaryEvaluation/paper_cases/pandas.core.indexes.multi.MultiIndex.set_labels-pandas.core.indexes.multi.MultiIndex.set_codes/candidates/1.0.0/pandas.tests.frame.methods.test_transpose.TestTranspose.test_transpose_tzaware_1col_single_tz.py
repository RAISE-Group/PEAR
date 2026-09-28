def test_transpose_tzaware_1col_single_tz(self):
    dti = pd.date_range('2016-04-05 04:30', periods=3, tz='UTC')
    df = pd.DataFrame(dti)
    assert (df.dtypes == dti.dtype).all()
    res = df.T
    assert (res.dtypes == dti.dtype).all()