def test_to_records_dict_like(self):

    class DictLike:

        def __init__(self, **kwargs):
            self.d = kwargs.copy()

        def __getitem__(self, key):
            return self.d.__getitem__(key)

        def __contains__(self, key) -> bool:
            return key in self.d

        def keys(self):
            return self.d.keys()
    df = DataFrame({'A': [1, 2], 'B': [0.2, 1.5], 'C': ['a', 'bc']})
    dtype_mappings = dict(column_dtypes=DictLike(**{'A': np.int8, 'B': np.float32}), index_dtypes='<U2')
    result = df.to_records(**dtype_mappings)
    expected = np.rec.array([('0', '1', '0.2', 'a'), ('1', '2', '1.5', 'bc')], dtype=[('index', '<U2'), ('A', 'i1'), ('B', '<f4'), ('C', 'O')])
    tm.assert_almost_equal(result, expected)