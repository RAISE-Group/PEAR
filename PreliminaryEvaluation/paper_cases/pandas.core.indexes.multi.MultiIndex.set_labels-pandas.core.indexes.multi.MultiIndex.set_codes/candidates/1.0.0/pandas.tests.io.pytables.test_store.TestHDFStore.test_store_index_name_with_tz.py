def test_store_index_name_with_tz(self, setup_path):
    df = pd.DataFrame({'A': [1, 2]})
    df.index = pd.DatetimeIndex([1234567890123456787, 1234567890123456788])
    df.index = df.index.tz_localize('UTC')
    df.index.name = 'foo'
    with ensure_clean_store(setup_path) as store:
        store.put('frame', df, format='table')
        recons = store['frame']
        tm.assert_frame_equal(recons, df)