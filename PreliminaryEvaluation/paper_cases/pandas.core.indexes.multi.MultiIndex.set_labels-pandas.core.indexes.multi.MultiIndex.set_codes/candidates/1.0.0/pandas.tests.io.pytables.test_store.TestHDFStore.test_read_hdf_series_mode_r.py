@pytest.mark.parametrize('format', ['fixed', 'table'])
def test_read_hdf_series_mode_r(self, format, setup_path):
    series = tm.makeFloatSeries()
    with ensure_clean_path(setup_path) as path:
        series.to_hdf(path, key='data', format=format)
        result = pd.read_hdf(path, key='data', mode='r')
    tm.assert_series_equal(result, series)