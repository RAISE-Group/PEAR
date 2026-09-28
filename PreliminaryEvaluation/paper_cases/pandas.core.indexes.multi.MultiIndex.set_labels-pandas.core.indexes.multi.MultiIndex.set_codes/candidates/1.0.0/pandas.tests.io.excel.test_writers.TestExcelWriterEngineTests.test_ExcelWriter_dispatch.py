@pytest.mark.parametrize('klass,ext', [pytest.param(_XlsxWriter, '.xlsx', marks=td.skip_if_no('xlsxwriter')), pytest.param(_OpenpyxlWriter, '.xlsx', marks=td.skip_if_no('openpyxl')), pytest.param(_XlwtWriter, '.xls', marks=td.skip_if_no('xlwt'))])
def test_ExcelWriter_dispatch(self, klass, ext):
    with tm.ensure_clean(ext) as path:
        writer = ExcelWriter(path)
        if ext == '.xlsx' and td.safe_import('xlsxwriter'):
            assert isinstance(writer, _XlsxWriter)
        else:
            assert isinstance(writer, klass)