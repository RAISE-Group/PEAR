def test_astype_uint(self):
    arr = date_range('2000', periods=2)
    expected = pd.UInt64Index(np.array([946684800000000000, 946771200000000000], dtype='uint64'))
    tm.assert_index_equal(arr.astype('uint64'), expected)
    tm.assert_index_equal(arr.astype('uint32'), expected)