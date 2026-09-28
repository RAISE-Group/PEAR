def test_select_iterator_complete_8014(self, setup_path):
    chunksize = 10000.0
    with ensure_clean_store(setup_path) as store:
        expected = tm.makeTimeDataFrame(100064, 'S')
        _maybe_remove(store, 'df')
        store.append('df', expected)
        beg_dt = expected.index[0]
        end_dt = expected.index[-1]
        result = store.select('df')
        tm.assert_frame_equal(expected, result)
        where = "index >= '{beg_dt}'".format(beg_dt=beg_dt)
        result = store.select('df', where=where)
        tm.assert_frame_equal(expected, result)
        where = "index <= '{end_dt}'".format(end_dt=end_dt)
        result = store.select('df', where=where)
        tm.assert_frame_equal(expected, result)
        where = "index >= '{beg_dt}' & index <= '{end_dt}'".format(beg_dt=beg_dt, end_dt=end_dt)
        result = store.select('df', where=where)
        tm.assert_frame_equal(expected, result)
    with ensure_clean_store(setup_path) as store:
        expected = tm.makeTimeDataFrame(100064, 'S')
        _maybe_remove(store, 'df')
        store.append('df', expected)
        beg_dt = expected.index[0]
        end_dt = expected.index[-1]
        results = list(store.select('df', chunksize=chunksize))
        result = concat(results)
        tm.assert_frame_equal(expected, result)
        where = "index >= '{beg_dt}'".format(beg_dt=beg_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        result = concat(results)
        tm.assert_frame_equal(expected, result)
        where = "index <= '{end_dt}'".format(end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        result = concat(results)
        tm.assert_frame_equal(expected, result)
        where = "index >= '{beg_dt}' & index <= '{end_dt}'".format(beg_dt=beg_dt, end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        result = concat(results)
        tm.assert_frame_equal(expected, result)