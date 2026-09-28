@td.xfail_non_writeable
def test_legacy_table_fixed_format_read_py2(self, datapath, setup_path):
    with ensure_clean_store(datapath('io', 'data', 'legacy_hdf', 'legacy_table_fixed_py2.h5'), mode='r') as store:
        result = store.select('df')
        expected = pd.DataFrame([[1, 2, 3, 'D']], columns=['A', 'B', 'C', 'D'], index=pd.Index(['ABC'], name='INDEX_NAME'))
        tm.assert_frame_equal(expected, result)