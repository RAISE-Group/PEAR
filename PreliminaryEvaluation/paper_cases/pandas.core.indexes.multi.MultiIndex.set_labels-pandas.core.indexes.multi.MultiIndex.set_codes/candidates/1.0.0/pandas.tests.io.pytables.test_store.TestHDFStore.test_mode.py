def test_mode(self, setup_path):
    df = tm.makeTimeDataFrame()

    def check(mode):
        with ensure_clean_path(setup_path) as path:
            if mode in ['r', 'r+']:
                with pytest.raises(IOError):
                    HDFStore(path, mode=mode)
            else:
                store = HDFStore(path, mode=mode)
                assert store._handle.mode == mode
                store.close()
        with ensure_clean_path(setup_path) as path:
            if mode in ['r', 'r+']:
                with pytest.raises(IOError):
                    with HDFStore(path, mode=mode) as store:
                        pass
            else:
                with HDFStore(path, mode=mode) as store:
                    assert store._handle.mode == mode
        with ensure_clean_path(setup_path) as path:
            if mode in ['r', 'r+']:
                with pytest.raises(IOError):
                    df.to_hdf(path, 'df', mode=mode)
                df.to_hdf(path, 'df', mode='w')
            else:
                df.to_hdf(path, 'df', mode=mode)
            if mode in ['w']:
                msg = 'mode w is not allowed while performing a read. Allowed modes are r, r\\+ and a.'
                with pytest.raises(ValueError, match=msg):
                    read_hdf(path, 'df', mode=mode)
            else:
                result = read_hdf(path, 'df', mode=mode)
                tm.assert_frame_equal(result, df)

    def check_default_mode():
        with ensure_clean_path(setup_path) as path:
            df.to_hdf(path, 'df', mode='w')
            result = read_hdf(path, 'df')
            tm.assert_frame_equal(result, df)
    check('r')
    check('r+')
    check('a')
    check('w')
    check_default_mode()