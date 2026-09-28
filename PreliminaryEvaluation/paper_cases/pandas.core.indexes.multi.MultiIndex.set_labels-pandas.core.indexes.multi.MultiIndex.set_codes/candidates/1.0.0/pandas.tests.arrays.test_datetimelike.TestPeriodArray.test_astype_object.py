def test_astype_object(self, period_index):
    pi = period_index
    arr = PeriodArray(pi)
    asobj = arr.astype('O')
    assert isinstance(asobj, np.ndarray)
    assert asobj.dtype == 'O'
    assert list(asobj) == list(pi)