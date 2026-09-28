def test_reader_special_dtypes(self, read_ext):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    expected = DataFrame.from_dict(OrderedDict([('IntCol', [1, 2, -3, 4, 0]), ('FloatCol', [1.25, 2.25, 1.83, 1.92, 5e-10]), ('BoolCol', [True, False, True, True, False]), ('StrCol', [1, 2, 3, 4, 5]), ('Str2Col', ['a', 3, 'c', 'd', 'e']), ('DateCol', [datetime(2013, 10, 30), datetime(2013, 10, 31), datetime(1905, 1, 1), datetime(2013, 12, 14), datetime(2015, 3, 14)])]))
    basename = 'test_types'
    actual = pd.read_excel(basename + read_ext, 'Sheet1')
    tm.assert_frame_equal(actual, expected)
    float_expected = expected.copy()
    float_expected['IntCol'] = float_expected['IntCol'].astype(float)
    float_expected.loc[float_expected.index[1], 'Str2Col'] = 3.0
    actual = pd.read_excel(basename + read_ext, 'Sheet1', convert_float=False)
    tm.assert_frame_equal(actual, float_expected)
    for icol, name in enumerate(expected.columns):
        actual = pd.read_excel(basename + read_ext, 'Sheet1', index_col=icol)
        exp = expected.set_index(name)
        tm.assert_frame_equal(actual, exp)
    expected['StrCol'] = expected['StrCol'].apply(str)
    actual = pd.read_excel(basename + read_ext, 'Sheet1', converters={'StrCol': str})
    tm.assert_frame_equal(actual, expected)
    no_convert_float = float_expected.copy()
    no_convert_float['StrCol'] = no_convert_float['StrCol'].apply(str)
    actual = pd.read_excel(basename + read_ext, 'Sheet1', convert_float=False, converters={'StrCol': str})
    tm.assert_frame_equal(actual, no_convert_float)