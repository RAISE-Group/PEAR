@pytest.mark.parametrize('sep', ['\t', None, 'default'])
@pytest.mark.parametrize('excel', [True, None, 'default'])
def test_clipboard_copy_tabs_default(self, sep, excel, df, request, mock_clipboard):
    kwargs = build_kwargs(sep, excel)
    df.to_clipboard(**kwargs)
    assert mock_clipboard[request.node.name] == df.to_csv(sep='\t')