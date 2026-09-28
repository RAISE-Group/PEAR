def test_start_stop_table(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(dict(A=np.random.rand(20), B=np.random.rand(20)))
        store.append('df', df)
        result = store.select('df', "columns=['A']", start=0, stop=5)
        expected = df.loc[0:4, ['A']]
        tm.assert_frame_equal(result, expected)
        result = store.select('df', "columns=['A']", start=30, stop=40)
        assert len(result) == 0
        expected = df.loc[30:40, ['A']]
        tm.assert_frame_equal(result, expected)