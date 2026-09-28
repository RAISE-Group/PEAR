def test_reindex_astype_order_consistency(self):
    s = Series([1, 2, 3], index=[2, 0, 1])
    new_index = [0, 1, 2]
    temp_dtype = 'category'
    new_dtype = str
    s1 = s.reindex(new_index).astype(temp_dtype).astype(new_dtype)
    s2 = s.astype(temp_dtype).reindex(new_index).astype(new_dtype)
    tm.assert_series_equal(s1, s2)