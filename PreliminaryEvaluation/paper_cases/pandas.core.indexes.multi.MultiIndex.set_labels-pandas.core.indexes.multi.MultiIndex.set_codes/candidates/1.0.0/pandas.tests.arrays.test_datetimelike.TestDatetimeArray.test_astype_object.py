def test_astype_object(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    arr = DatetimeArray(dti)
    asobj = arr.astype('O')
    assert isinstance(asobj, np.ndarray)
    assert asobj.dtype == 'O'
    assert list(asobj) == list(dti)