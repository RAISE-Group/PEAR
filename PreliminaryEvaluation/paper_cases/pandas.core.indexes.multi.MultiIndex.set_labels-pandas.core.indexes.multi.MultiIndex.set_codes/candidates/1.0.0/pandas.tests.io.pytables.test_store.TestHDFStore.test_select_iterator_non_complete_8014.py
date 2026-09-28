def test_select_iterator_non_complete_8014(self, setup_path):
    chunksize = 10000.0
    with ensure_clean_store(setup_path) as store:
        expected = tm.makeTimeDataFrame(100064, 'S')
        _maybe_remove(store, 'df')
        store.append('df', expected)
        beg_dt = expected.index[1]
        end_dt = expected.index[-2]
        where = "index >= '{beg_dt}'".format(beg_dt=beg_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        result = concat(results)
        rexpected = expected[expected.index >= beg_dt]
        tm.assert_frame_equal(rexpected, result)
        where = "index <= '{end_dt}'".format(end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        result = concat(results)
        rexpected = expected[expected.index <= end_dt]
        tm.assert_frame_equal(rexpected, result)
        where = "index >= '{beg_dt}' & index <= '{end_dt}'".format(beg_dt=beg_dt, end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        result = concat(results)
        rexpected = expected[(expected.index >= beg_dt) & (expected.index <= end_dt)]
        tm.assert_frame_equal(rexpected, result)
    with ensure_clean_store(setup_path) as store:
        expected = tm.makeTimeDataFrame(100064, 'S')
        _maybe_remove(store, 'df')
        store.append('df', expected)
        end_dt = expected.index[-1]
        where = "index > '{end_dt}'".format(end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        assert 0 == len(results)