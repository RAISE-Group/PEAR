def test_flush(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        store['a'] = tm.makeTimeSeries()
        store.flush()
        store.flush(fsync=True)