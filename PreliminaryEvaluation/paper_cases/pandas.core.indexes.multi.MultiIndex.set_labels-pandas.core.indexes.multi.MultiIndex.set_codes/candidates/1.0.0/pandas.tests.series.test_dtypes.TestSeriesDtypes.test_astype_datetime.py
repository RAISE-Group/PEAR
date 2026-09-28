def test_astype_datetime(self):
    s = Series(iNaT, dtype='M8[ns]', index=range(5))
    s = s.astype('O')
    assert s.dtype == np.object_
    s = Series([datetime(2001, 1, 2, 0, 0)])
    s = s.astype('O')
    assert s.dtype == np.object_
    s = Series([datetime(2001, 1, 2, 0, 0) for i in range(3)])
    s[1] = np.nan
    assert s.dtype == 'M8[ns]'
    s = s.astype('O')
    assert s.dtype == np.object_