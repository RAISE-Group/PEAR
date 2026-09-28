def test_from_tzaware_object_array(self):
    dti = pd.date_range('2016-04-05 04:30', periods=3, tz='UTC')
    data = dti._data.astype(object).reshape(1, -1)
    df = pd.DataFrame(data)
    assert df.shape == (1, 3)
    assert (df.dtypes == dti.dtype).all()
    assert (df == dti).all().all()