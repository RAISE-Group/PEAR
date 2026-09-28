def test_frame_select(self, setup_path):
    df = tm.makeTimeDataFrame()
    with ensure_clean_store(setup_path) as store:
        store.put('frame', df, format='table')
        date = df.index[len(df) // 2]
        crit1 = Term('index>=date')
        assert crit1.env.scope['date'] == date
        crit2 = "columns=['A', 'D']"
        crit3 = 'columns=A'
        result = store.select('frame', [crit1, crit2])
        expected = df.loc[date:, ['A', 'D']]
        tm.assert_frame_equal(result, expected)
        result = store.select('frame', [crit3])
        expected = df.loc[:, ['A']]
        tm.assert_frame_equal(result, expected)
        df = tm.makeTimeDataFrame()
        store.append('df_time', df)
        with pytest.raises(ValueError):
            store.select('df_time', 'index>0')