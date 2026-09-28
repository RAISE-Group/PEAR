def test_astype_uint(self):
    arr = period_range('2000', periods=2)
    expected = pd.UInt64Index(np.array([10957, 10958], dtype='uint64'))
    tm.assert_index_equal(arr.astype('uint64'), expected)
    tm.assert_index_equal(arr.astype('uint32'), expected)