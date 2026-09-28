def test_read_excel_multiindex_header_only(self, read_ext):
    mi_file = 'testmultiindex' + read_ext
    result = pd.read_excel(mi_file, 'index_col_none', header=[0, 1])
    exp_columns = MultiIndex.from_product([('A', 'B'), ('key', 'val')])
    expected = DataFrame([[1, 2, 3, 4]] * 2, columns=exp_columns)
    tm.assert_frame_equal(result, expected)