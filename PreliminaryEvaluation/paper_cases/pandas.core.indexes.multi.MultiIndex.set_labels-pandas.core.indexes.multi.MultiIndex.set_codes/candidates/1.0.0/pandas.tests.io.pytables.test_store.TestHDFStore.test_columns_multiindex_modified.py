def test_columns_multiindex_modified(self, setup_path):
    df = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    df.index.name = 'letters'
    df = df.set_index(keys='E', append=True)
    data_columns = df.index.names + df.columns.tolist()
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', mode='a', append=True, data_columns=data_columns, index=False)
        cols2load = list('BCD')
        cols2load_original = list(cols2load)
        df_loaded = read_hdf(path, 'df', columns=cols2load)
        assert cols2load_original == cols2load