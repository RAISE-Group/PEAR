def test_read_py2_hdf_file_in_py3(self, datapath):
    expected = pd.DataFrame([1.0, 2, 3], index=pd.PeriodIndex(['2015-01-01', '2015-01-02', '2015-01-05'], freq='B'))
    with ensure_clean_store(datapath('io', 'data', 'legacy_hdf', 'periodindex_0.20.1_x86_64_darwin_2.7.13.h5'), mode='r') as store:
        result = store['p']
        tm.assert_frame_equal(result, expected)