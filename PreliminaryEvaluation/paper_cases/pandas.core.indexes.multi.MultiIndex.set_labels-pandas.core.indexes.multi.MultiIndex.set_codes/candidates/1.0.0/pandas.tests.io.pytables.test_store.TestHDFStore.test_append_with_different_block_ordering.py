def test_append_with_different_block_ordering(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        for i in range(10):
            df = DataFrame(np.random.randn(10, 2), columns=list('AB'))
            df['index'] = range(10)
            df['index'] += i * 10
            df['int64'] = Series([1] * len(df), dtype='int64')
            df['int16'] = Series([1] * len(df), dtype='int16')
            if i % 2 == 0:
                del df['int64']
                df['int64'] = Series([1] * len(df), dtype='int64')
            if i % 3 == 0:
                a = df.pop('A')
                df['A'] = a
            df.set_index('index', inplace=True)
            store.append('df', df)
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(np.random.randn(10, 2), columns=list('AB'), dtype='float64')
        df['int64'] = Series([1] * len(df), dtype='int64')
        df['int16'] = Series([1] * len(df), dtype='int16')
        store.append('df', df)
        df['int16_2'] = Series([1] * len(df), dtype='int16')
        with pytest.raises(ValueError):
            store.append('df', df)
        df['float_3'] = Series([1.0] * len(df), dtype='float64')
        with pytest.raises(ValueError):
            store.append('df', df)