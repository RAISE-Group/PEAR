@pytest.mark.parametrize('reader, module, path', [(pd.read_csv, 'os', ('data', 'iris.csv')), (pd.read_table, 'os', ('data', 'iris.csv')), (pd.read_fwf, 'os', ('io', 'data', 'fixed_width', 'fixed_width_format.txt')), (pd.read_excel, 'xlrd', ('io', 'data', 'excel', 'test1.xlsx')), (pd.read_feather, 'feather', ('io', 'data', 'feather', 'feather-0_3_1.feather')), (pd.read_hdf, 'tables', ('io', 'data', 'legacy_hdf', 'datetimetz_object.h5')), (pd.read_stata, 'os', ('io', 'data', 'stata', 'stata10_115.dta')), (pd.read_sas, 'os', ('io', 'sas', 'data', 'test1.sas7bdat')), (pd.read_json, 'os', ('io', 'json', 'data', 'tsframe_v012.json')), (pd.read_pickle, 'os', ('io', 'data', 'pickle', 'categorical.0.25.0.pickle'))])
def test_read_fspath_all(self, reader, module, path, datapath):
    pytest.importorskip(module)
    path = datapath(*path)
    mypath = CustomFSPath(path)
    result = reader(mypath)
    expected = reader(path)
    if path.endswith('.pickle'):
        tm.assert_categorical_equal(result, expected)
    else:
        tm.assert_frame_equal(result, expected)