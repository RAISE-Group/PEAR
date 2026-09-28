def test_invalid_filtering(self, setup_path):
    df = tm.makeTimeDataFrame()
    with ensure_clean_store(setup_path) as store:
        store.put('df', df, format='table')
        with pytest.raises(NotImplementedError):
            store.select('df', "columns=['A'] | columns=['B']")
        with pytest.raises(NotImplementedError):
            store.select('df', "columns=['A','B'] & columns=['C']")