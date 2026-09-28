def test_usecols_excel_range_str_invalid(self, read_ext):
    msg = 'Invalid column name: E1'
    with pytest.raises(ValueError, match=msg):
        pd.read_excel('test1' + read_ext, 'Sheet1', usecols='D:E1')