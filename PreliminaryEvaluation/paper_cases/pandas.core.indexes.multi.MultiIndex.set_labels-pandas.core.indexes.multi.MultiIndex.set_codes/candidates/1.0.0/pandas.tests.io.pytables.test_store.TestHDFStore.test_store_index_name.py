def test_store_index_name(self, setup_path):
    df = tm.makeDataFrame()
    df.index.name = 'foo'
    with ensure_clean_store(setup_path) as store:
        store['frame'] = df
        recons = store['frame']
        tm.assert_frame_equal(recons, df)