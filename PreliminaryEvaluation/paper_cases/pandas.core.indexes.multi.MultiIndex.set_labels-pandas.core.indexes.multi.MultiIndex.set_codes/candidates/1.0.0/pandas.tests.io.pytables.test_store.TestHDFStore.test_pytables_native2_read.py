@pytest.mark.skipif(is_platform_windows(), reason='native2 read fails oddly on windows')
def test_pytables_native2_read(self, datapath, setup_path):
    with ensure_clean_store(datapath('io', 'data', 'legacy_hdf', 'pytables_native2.h5'), mode='r') as store:
        str(store)
        d1 = store['detector']
        assert isinstance(d1, DataFrame)