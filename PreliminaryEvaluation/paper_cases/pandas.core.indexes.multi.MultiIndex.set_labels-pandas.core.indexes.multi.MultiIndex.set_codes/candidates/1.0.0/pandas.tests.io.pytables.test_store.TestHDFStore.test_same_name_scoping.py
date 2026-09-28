def test_same_name_scoping(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        import pandas as pd
        df = DataFrame(np.random.randn(20, 2), index=pd.date_range('20130101', periods=20))
        store.put('df', df, format='table')
        expected = df[df.index > pd.Timestamp('20130105')]
        import datetime
        result = store.select('df', 'index>datetime.datetime(2013,1,5)')
        tm.assert_frame_equal(result, expected)
        from datetime import datetime
        result = store.select('df', 'index>datetime.datetime(2013,1,5)')
        tm.assert_frame_equal(result, expected)
        result = store.select('df', 'index>datetime(2013,1,5)')
        tm.assert_frame_equal(result, expected)