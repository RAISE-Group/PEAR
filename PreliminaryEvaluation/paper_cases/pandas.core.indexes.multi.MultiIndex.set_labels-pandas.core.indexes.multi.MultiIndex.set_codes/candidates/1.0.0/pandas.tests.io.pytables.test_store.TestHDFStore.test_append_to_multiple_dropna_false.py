@pytest.mark.xfail(run=False, reason='append_to_multiple_dropna_false is not raising as failed')
def test_append_to_multiple_dropna_false(self, setup_path):
    df1 = tm.makeTimeDataFrame()
    df2 = tm.makeTimeDataFrame().rename(columns='{}_2'.format)
    df1.iloc[1, df1.columns.get_indexer(['A', 'B'])] = np.nan
    df = concat([df1, df2], axis=1)
    with ensure_clean_store(setup_path) as store:
        store.append_to_multiple({'df1a': ['A', 'B'], 'df2a': None}, df, selector='df1a', dropna=False)
        with pytest.raises(ValueError):
            store.select_as_multiple(['df1a', 'df2a'])
        assert not store.select('df1a').index.equals(store.select('df2a').index)