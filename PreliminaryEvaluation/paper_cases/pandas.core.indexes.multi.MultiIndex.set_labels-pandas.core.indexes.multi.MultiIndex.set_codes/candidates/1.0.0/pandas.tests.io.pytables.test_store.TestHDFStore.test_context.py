def test_context(self, setup_path):
    path = create_tempfile(setup_path)
    try:
        with HDFStore(path) as tbl:
            raise ValueError('blah')
    except ValueError:
        pass
    finally:
        safe_remove(path)
    try:
        with HDFStore(path) as tbl:
            tbl['a'] = tm.makeDataFrame()
        with HDFStore(path) as tbl:
            assert len(tbl) == 1
            assert type(tbl['a']) == DataFrame
    finally:
        safe_remove(path)