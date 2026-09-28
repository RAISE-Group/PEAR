@pytest.mark.parametrize('writer_name, writer_kwargs, module', [('to_csv', {}, 'os'), ('to_excel', {'engine': 'xlwt'}, 'xlwt'), ('to_feather', {}, 'feather'), ('to_html', {}, 'os'), ('to_json', {}, 'os'), ('to_latex', {}, 'os'), ('to_pickle', {}, 'os'), ('to_stata', {'time_stamp': pd.to_datetime('2019-01-01 00:00')}, 'os')])
def test_write_fspath_all(self, writer_name, writer_kwargs, module):
    p1 = tm.ensure_clean('string')
    p2 = tm.ensure_clean('fspath')
    df = pd.DataFrame({'A': [1, 2]})
    with p1 as string, p2 as fspath:
        pytest.importorskip(module)
        mypath = CustomFSPath(fspath)
        writer = getattr(df, writer_name)
        writer(string, **writer_kwargs)
        with open(string, 'rb') as f:
            expected = f.read()
        writer(mypath, **writer_kwargs)
        with open(fspath, 'rb') as f:
            result = f.read()
        assert result == expected