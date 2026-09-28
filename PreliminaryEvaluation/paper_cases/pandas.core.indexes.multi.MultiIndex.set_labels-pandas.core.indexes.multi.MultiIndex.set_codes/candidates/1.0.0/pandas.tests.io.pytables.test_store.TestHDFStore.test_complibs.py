def test_complibs(self, setup_path):
    df = tm.makeDataFrame()
    all_complibs = tables.filters.all_complibs
    if not tables.which_lib_version('lzo'):
        all_complibs.remove('lzo')
    if not tables.which_lib_version('bzip2'):
        all_complibs.remove('bzip2')
    all_levels = range(0, 10)
    all_tests = [(lib, lvl) for lib in all_complibs for lvl in all_levels]
    for lib, lvl in all_tests:
        with ensure_clean_path(setup_path) as tmpfile:
            gname = 'foo'
            df.to_hdf(tmpfile, gname, complib=lib, complevel=lvl)
            result = pd.read_hdf(tmpfile, gname)
            tm.assert_frame_equal(result, df)
            h5table = tables.open_file(tmpfile, mode='r')
            for node in h5table.walk_nodes(where='/' + gname, classname='Leaf'):
                assert node.filters.complevel == lvl
                if lvl == 0:
                    assert node.filters.complib is None
                else:
                    assert node.filters.complib == lib
            h5table.close()