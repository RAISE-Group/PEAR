@pytest.mark.parametrize('arg', ['sheet', 'sheetname', 'parse_cols'])
@td.check_file_leaks
def test_unexpected_kwargs_raises(self, read_ext, arg):
    kwarg = {arg: 'Sheet1'}
    msg = 'unexpected keyword argument `{}`'.format(arg)
    with pd.ExcelFile('test1' + read_ext) as excel:
        with pytest.raises(TypeError, match=msg):
            pd.read_excel(excel, **kwarg)