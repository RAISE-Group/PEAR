def test_pass_spec_to_storer(self, setup_path):
    df = tm.makeDataFrame()
    with ensure_clean_store(setup_path) as store:
        store.put('df', df)
        with pytest.raises(TypeError):
            store.select('df', columns=['A'])
        with pytest.raises(TypeError):
            store.select('df', where=['columns=A'])