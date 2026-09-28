def test_usecols_pass_non_existent_column(self, read_ext):
    msg = 'Usecols do not match columns, columns expected but not found: ' + "\\['E'\\]"
    with pytest.raises(ValueError, match=msg):
        pd.read_excel('test1' + read_ext, usecols=['E'])