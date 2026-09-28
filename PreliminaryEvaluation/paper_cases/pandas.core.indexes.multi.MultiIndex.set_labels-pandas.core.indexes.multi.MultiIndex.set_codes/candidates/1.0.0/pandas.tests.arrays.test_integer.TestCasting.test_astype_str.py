def test_astype_str(self):
    a = pd.array([1, 2, None], dtype='Int64')
    expected = np.array(['1', '2', '<NA>'], dtype=object)
    tm.assert_numpy_array_equal(a.astype(str), expected)
    tm.assert_numpy_array_equal(a.astype('str'), expected)