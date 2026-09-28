def test_store_series_name(self, setup_path):
    df = tm.makeDataFrame()
    series = df['A']
    with ensure_clean_store(setup_path) as store:
        store['series'] = series
        recons = store['series']
        tm.assert_series_equal(recons, series)