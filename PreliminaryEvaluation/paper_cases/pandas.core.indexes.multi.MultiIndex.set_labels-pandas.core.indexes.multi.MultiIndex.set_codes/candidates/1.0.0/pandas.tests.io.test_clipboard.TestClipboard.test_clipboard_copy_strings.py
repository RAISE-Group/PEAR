@pytest.mark.parametrize('sep', [None, 'default'])
@pytest.mark.parametrize('excel', [False])
def test_clipboard_copy_strings(self, sep, excel, df):
    kwargs = build_kwargs(sep, excel)
    df.to_clipboard(**kwargs)
    result = read_clipboard(sep='\\s+')
    assert result.to_string() == df.to_string()
    assert df.shape == result.shape