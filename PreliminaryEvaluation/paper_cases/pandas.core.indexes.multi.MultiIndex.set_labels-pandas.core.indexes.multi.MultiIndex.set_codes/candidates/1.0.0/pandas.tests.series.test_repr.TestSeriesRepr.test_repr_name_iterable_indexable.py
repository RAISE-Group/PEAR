def test_repr_name_iterable_indexable(self):
    s = Series([1, 2, 3], name=np.int64(3))
    repr(s)
    s.name = ('א',) * 2
    repr(s)