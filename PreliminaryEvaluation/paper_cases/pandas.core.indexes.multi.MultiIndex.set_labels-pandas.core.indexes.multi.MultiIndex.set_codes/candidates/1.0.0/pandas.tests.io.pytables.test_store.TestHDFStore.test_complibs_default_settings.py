def test_complibs_default_settings(self, setup_path):
    df = tm.makeDataFrame()
    with ensure_clean_path(setup_path) as tmpfile:
        df.to_hdf(tmpfile, 'df', complevel=9)
        result = pd.read_hdf(tmpfile, 'df')
        tm.assert_frame_equal(result, df)
        with tables.open_file(tmpfile, mode='r') as h5file:
            for node in h5file.walk_nodes(where='/df', classname='Leaf'):
                assert node.filters.complevel == 9
                assert node.filters.complib == 'zlib'
    with ensure_clean_path(setup_path) as tmpfile:
        df.to_hdf(tmpfile, 'df', complib='zlib')
        result = pd.read_hdf(tmpfile, 'df')
        tm.assert_frame_equal(result, df)
        with tables.open_file(tmpfile, mode='r') as h5file:
            for node in h5file.walk_nodes(where='/df', classname='Leaf'):
                assert node.filters.complevel == 0
                assert node.filters.complib is None
    with ensure_clean_path(setup_path) as tmpfile:
        df.to_hdf(tmpfile, 'df')
        result = pd.read_hdf(tmpfile, 'df')
        tm.assert_frame_equal(result, df)
        with tables.open_file(tmpfile, mode='r') as h5file:
            for node in h5file.walk_nodes(where='/df', classname='Leaf'):
                assert node.filters.complevel == 0
                assert node.filters.complib is None
    with ensure_clean_path(setup_path) as tmpfile:
        store = pd.HDFStore(tmpfile)
        store.append('dfc', df, complevel=9, complib='blosc')
        store.append('df', df)
        store.close()
        with tables.open_file(tmpfile, mode='r') as h5file:
            for node in h5file.walk_nodes(where='/df', classname='Leaf'):
                assert node.filters.complevel == 0
                assert node.filters.complib is None
            for node in h5file.walk_nodes(where='/dfc', classname='Leaf'):
                assert node.filters.complevel == 9
                assert node.filters.complib == 'blosc'