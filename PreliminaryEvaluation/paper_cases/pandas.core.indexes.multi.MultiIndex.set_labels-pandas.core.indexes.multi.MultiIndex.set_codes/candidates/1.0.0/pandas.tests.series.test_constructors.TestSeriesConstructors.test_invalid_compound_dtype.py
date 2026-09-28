def test_invalid_compound_dtype(self):
    c_dtype = np.dtype([('a', 'i8'), ('b', 'f4')])
    cdt_arr = np.array([(1, 0.4), (256, -13)], dtype=c_dtype)
    with pytest.raises(ValueError, match='Use DataFrame instead'):
        Series(cdt_arr, index=['A', 'B'])