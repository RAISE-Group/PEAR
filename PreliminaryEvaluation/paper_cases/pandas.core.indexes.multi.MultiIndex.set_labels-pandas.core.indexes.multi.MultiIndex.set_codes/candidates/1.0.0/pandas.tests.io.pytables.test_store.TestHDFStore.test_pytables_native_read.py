def test_pytables_native_read(self, datapath, setup_path):
    with ensure_clean_store(datapath('io', 'data', 'legacy_hdf/pytables_native.h5'), mode='r') as store:
        d2 = store['detector/readout']
        assert isinstance(d2, DataFrame)