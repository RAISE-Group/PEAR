def test_unicode_longer_encoded(self, setup_path):
    char = 'Δ'
    df = pd.DataFrame({'A': [char]})
    with ensure_clean_store(setup_path) as store:
        store.put('df', df, format='table', encoding='utf-8')
        result = store.get('df')
        tm.assert_frame_equal(result, df)
    df = pd.DataFrame({'A': ['a', char], 'B': ['b', 'b']})
    with ensure_clean_store(setup_path) as store:
        store.put('df', df, format='table', encoding='utf-8')
        result = store.get('df')
        tm.assert_frame_equal(result, df)