def test_usecols_wrong_type(self, read_ext):
    msg = "'usecols' must either be list-like of all strings, all unicode, all integers or a callable."
    with pytest.raises(ValueError, match=msg):
        pd.read_excel('test1' + read_ext, usecols=['E1', 0])