@pytest.mark.parametrize('where', ['', (), (None,), [], [None]])
def test_select_empty_where(self, where):
    df = pd.DataFrame([1, 2, 3])
    with ensure_clean_path('empty_where.h5') as path:
        with pd.HDFStore(path) as store:
            store.put('df', df, 't')
            result = pd.read_hdf(store, 'df', where=where)
            tm.assert_frame_equal(result, df)