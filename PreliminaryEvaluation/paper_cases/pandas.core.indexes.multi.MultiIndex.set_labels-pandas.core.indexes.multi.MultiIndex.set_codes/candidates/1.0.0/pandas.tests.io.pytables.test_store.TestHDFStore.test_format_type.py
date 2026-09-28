def test_format_type(self, setup_path):
    df = pd.DataFrame({'A': [1, 2]})
    with ensure_clean_path(setup_path) as path:
        with HDFStore(path) as store:
            store.put('a', df, format='fixed')
            store.put('b', df, format='table')
            assert store.get_storer('a').format_type == 'fixed'
            assert store.get_storer('b').format_type == 'table'