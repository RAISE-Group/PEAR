def test_astype_object(self):
    tdi = pd.TimedeltaIndex(['1 Day', '3 Hours'])
    arr = TimedeltaArray(tdi)
    asobj = arr.astype('O')
    assert isinstance(asobj, np.ndarray)
    assert asobj.dtype == 'O'
    assert list(asobj) == list(tdi)