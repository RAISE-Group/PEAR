@pytest.mark.parametrize('format', [pytest.param('fixed', marks=td.xfail_non_writeable), 'table'])
def test_to_hdf_errors(self, format, setup_path):
    data = ['\ud800foo']
    ser = pd.Series(data, index=pd.Index(data))
    with ensure_clean_path(setup_path) as path:
        ser.to_hdf(path, 'table', format=format, errors='surrogatepass')
        result = pd.read_hdf(path, 'table', errors='surrogatepass')
        tm.assert_series_equal(result, ser)