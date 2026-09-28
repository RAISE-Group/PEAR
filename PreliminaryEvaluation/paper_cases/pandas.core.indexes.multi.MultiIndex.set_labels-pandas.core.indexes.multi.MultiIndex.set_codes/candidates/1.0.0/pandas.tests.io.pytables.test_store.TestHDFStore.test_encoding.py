@pytest.mark.skipif(not is_platform_little_endian(), reason='reason platform is not little endian')
def test_encoding(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(dict(A='foo', B='bar'), index=range(5))
        df.loc[2, 'A'] = np.nan
        df.loc[3, 'B'] = np.nan
        _maybe_remove(store, 'df')
        store.append('df', df, encoding='ascii')
        tm.assert_frame_equal(store['df'], df)
        expected = df.reindex(columns=['A'])
        result = store.select('df', Term('columns=A', encoding='ascii'))
        tm.assert_frame_equal(result, expected)