@pytest.mark.parametrize('reader, module, error_class, fn_ext', [(pd.read_csv, 'os', FileNotFoundError, 'csv'), (pd.read_table, 'os', FileNotFoundError, 'csv'), (pd.read_fwf, 'os', FileNotFoundError, 'txt'), (pd.read_excel, 'xlrd', FileNotFoundError, 'xlsx'), (pd.read_feather, 'feather', Exception, 'feather'), (pd.read_hdf, 'tables', FileNotFoundError, 'h5'), (pd.read_stata, 'os', FileNotFoundError, 'dta'), (pd.read_sas, 'os', FileNotFoundError, 'sas7bdat'), (pd.read_json, 'os', ValueError, 'json'), (pd.read_pickle, 'os', FileNotFoundError, 'pickle')])
def test_read_expands_user_home_dir(self, reader, module, error_class, fn_ext, monkeypatch):
    pytest.importorskip(module)
    path = os.path.join('~', 'does_not_exist.' + fn_ext)
    monkeypatch.setattr(icom, '_expand_user', lambda x: os.path.join('foo', x))
    msg1 = f"File (b')?.+does_not_exist\\.{fn_ext}'? does not exist"
    msg2 = f"\\[Errno 2\\] No such file or directory: '.+does_not_exist\\.{fn_ext}'"
    msg3 = "Unexpected character found when decoding 'false'"
    msg4 = 'path_or_buf needs to be a string file path or file-like'
    msg5 = f"\\[Errno 2\\] File .+does_not_exist\\.{fn_ext} does not exist: '.+does_not_exist\\.{fn_ext}'"
    msg6 = f"\\[Errno 2\\] 没有那个文件或目录: '.+does_not_exist\\.{fn_ext}'"
    msg7 = f"\\[Errno 2\\] File o directory non esistente: '.+does_not_exist\\.{fn_ext}'"
    with pytest.raises(error_class, match=f'({msg1}|{msg2}|{msg3}|{msg4}|{msg5}|{msg6}|{msg7})'):
        reader(path)