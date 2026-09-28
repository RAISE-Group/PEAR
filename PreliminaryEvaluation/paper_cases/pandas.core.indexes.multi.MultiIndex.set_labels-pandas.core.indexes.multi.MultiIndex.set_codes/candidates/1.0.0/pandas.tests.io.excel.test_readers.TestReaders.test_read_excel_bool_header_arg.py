def test_read_excel_bool_header_arg(self, read_ext):
    for arg in [True, False]:
        with pytest.raises(TypeError):
            pd.read_excel('test1' + read_ext, header=arg)