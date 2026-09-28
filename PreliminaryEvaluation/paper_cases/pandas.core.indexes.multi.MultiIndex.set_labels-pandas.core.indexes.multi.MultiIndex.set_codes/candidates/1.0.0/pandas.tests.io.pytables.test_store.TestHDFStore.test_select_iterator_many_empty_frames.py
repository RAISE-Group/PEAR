def test_select_iterator_many_empty_frames(self, setup_path):
    chunksize = int(10000.0)
    with ensure_clean_store(setup_path) as store:
        expected = tm.makeTimeDataFrame(100000, 'S')
        _maybe_remove(store, 'df')
        store.append('df', expected)
        beg_dt = expected.index[0]
        end_dt = expected.index[chunksize - 1]
        where = "index >= '{beg_dt}'".format(beg_dt=beg_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        result = concat(results)
        rexpected = expected[expected.index >= beg_dt]
        tm.assert_frame_equal(rexpected, result)
        where = "index <= '{end_dt}'".format(end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        assert len(results) == 1
        result = concat(results)
        rexpected = expected[expected.index <= end_dt]
        tm.assert_frame_equal(rexpected, result)
        where = "index >= '{beg_dt}' & index <= '{end_dt}'".format(beg_dt=beg_dt, end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        assert len(results) == 1
        result = concat(results)
        rexpected = expected[(expected.index >= beg_dt) & (expected.index <= end_dt)]
        tm.assert_frame_equal(rexpected, result)
        where = "index <= '{beg_dt}' & index >= '{end_dt}'".format(beg_dt=beg_dt, end_dt=end_dt)
        results = list(store.select('df', where=where, chunksize=chunksize))
        assert len(results) == 0