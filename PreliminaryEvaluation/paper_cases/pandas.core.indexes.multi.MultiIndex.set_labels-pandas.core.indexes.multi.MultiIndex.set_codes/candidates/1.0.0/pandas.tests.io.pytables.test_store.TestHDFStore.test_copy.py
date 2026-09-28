def test_copy(self, setup_path):
    with catch_warnings(record=True):

        def do_copy(f, new_f=None, keys=None, propindexes=True, **kwargs):
            try:
                store = HDFStore(f, 'r')
                if new_f is None:
                    import tempfile
                    fd, new_f = tempfile.mkstemp()
                tstore = store.copy(new_f, keys=keys, propindexes=propindexes, **kwargs)
                if keys is None:
                    keys = store.keys()
                assert set(keys) == set(tstore.keys())
                for k in tstore.keys():
                    if tstore.get_storer(k).is_table:
                        new_t = tstore.get_storer(k)
                        orig_t = store.get_storer(k)
                        assert orig_t.nrows == new_t.nrows
                        if propindexes:
                            for a in orig_t.axes:
                                if a.is_indexed:
                                    assert new_t[a.name].is_indexed
            finally:
                safe_close(store)
                safe_close(tstore)
                try:
                    os.close(fd)
                except (OSError, ValueError):
                    pass
                safe_remove(new_f)
        df = tm.makeDataFrame()
        try:
            path = create_tempfile(setup_path)
            st = HDFStore(path)
            st.append('df', df, data_columns=['A'])
            st.close()
            do_copy(f=path)
            do_copy(f=path, propindexes=False)
        finally:
            safe_remove(path)