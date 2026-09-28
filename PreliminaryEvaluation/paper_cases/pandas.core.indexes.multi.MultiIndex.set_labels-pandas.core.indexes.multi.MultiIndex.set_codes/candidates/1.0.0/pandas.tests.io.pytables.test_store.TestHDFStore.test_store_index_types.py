def test_store_index_types(self, setup_path):
    with ensure_clean_store(setup_path) as store:

        def check(format, index):
            df = DataFrame(np.random.randn(10, 2), columns=list('AB'))
            df.index = index(len(df))
            _maybe_remove(store, 'df')
            store.put('df', df, format=format)
            tm.assert_frame_equal(df, store['df'])
        for index in [tm.makeFloatIndex, tm.makeStringIndex, tm.makeIntIndex, tm.makeDateIndex]:
            check('table', index)
            check('fixed', index)
        check('fixed', tm.makePeriodIndex)
        index = tm.makeUnicodeIndex
        check('table', index)
        check('fixed', index)