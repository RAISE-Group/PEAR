def test_asarray_datetime64(self):
    s = SparseArray(pd.to_datetime(['2012', None, None, '2013']))
    np.asarray(s)