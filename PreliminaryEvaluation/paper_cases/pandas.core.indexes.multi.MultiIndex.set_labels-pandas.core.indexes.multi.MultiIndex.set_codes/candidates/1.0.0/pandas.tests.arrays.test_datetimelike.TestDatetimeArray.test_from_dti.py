def test_from_dti(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    arr = DatetimeArray(dti)
    assert list(dti) == list(arr)
    dti2 = pd.Index(arr)
    assert isinstance(dti2, pd.DatetimeIndex)
    assert list(dti2) == list(arr)