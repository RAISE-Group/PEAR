def test_read_excel_nrows_non_integer_parameter(self, read_ext):
    msg = "'nrows' must be an integer >=0"
    with pytest.raises(ValueError, match=msg):
        pd.read_excel('test1' + read_ext, nrows='5')