def test_astype_uint(self):
    arr = timedelta_range('1H', periods=2)
    expected = pd.UInt64Index(np.array([3600000000000, 90000000000000], dtype='uint64'))
    tm.assert_index_equal(arr.astype('uint64'), expected)
    tm.assert_index_equal(arr.astype('uint32'), expected)