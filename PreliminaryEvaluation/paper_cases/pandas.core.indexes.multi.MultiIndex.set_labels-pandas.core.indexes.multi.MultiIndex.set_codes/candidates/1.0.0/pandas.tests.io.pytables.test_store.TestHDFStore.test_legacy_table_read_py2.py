def test_legacy_table_read_py2(self, datapath, setup_path):
    with ensure_clean_store(datapath('io', 'data', 'legacy_hdf', 'legacy_table_py2.h5'), mode='r') as store:
        result = store.select('table')
    expected = pd.DataFrame({'a': ['a', 'b'], 'b': [2, 3]})
    tm.assert_frame_equal(expected, result)