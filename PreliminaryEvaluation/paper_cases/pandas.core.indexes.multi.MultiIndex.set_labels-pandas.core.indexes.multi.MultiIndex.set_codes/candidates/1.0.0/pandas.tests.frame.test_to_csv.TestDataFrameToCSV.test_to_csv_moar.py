@pytest.mark.slow
def test_to_csv_moar(self):

    def _do_test(df, r_dtype=None, c_dtype=None, rnlvl=None, cnlvl=None, dupe_col=False):
        kwargs = dict(parse_dates=False)
        if cnlvl:
            if rnlvl is not None:
                kwargs['index_col'] = list(range(rnlvl))
            kwargs['header'] = list(range(cnlvl))
            with tm.ensure_clean('__tmp_to_csv_moar__') as path:
                df.to_csv(path, encoding='utf8', chunksize=chunksize)
                recons = self.read_csv(path, **kwargs)
        else:
            kwargs['header'] = 0
            with tm.ensure_clean('__tmp_to_csv_moar__') as path:
                df.to_csv(path, encoding='utf8', chunksize=chunksize)
                recons = self.read_csv(path, **kwargs)

        def _to_uni(x):
            if not isinstance(x, str):
                return x.decode('utf8')
            return x
        if dupe_col:
            recons.columns = df.columns
        if rnlvl and (not cnlvl):
            delta_lvl = [recons.iloc[:, i].values for i in range(rnlvl - 1)]
            ix = MultiIndex.from_arrays([list(recons.index)] + delta_lvl)
            recons.index = ix
            recons = recons.iloc[:, rnlvl - 1:]
        type_map = dict(i='i', f='f', s='O', u='O', dt='O', p='O')
        if r_dtype:
            if r_dtype == 'u':
                r_dtype = 'O'
                recons.index = np.array([_to_uni(label) for label in recons.index], dtype=r_dtype)
                df.index = np.array([_to_uni(label) for label in df.index], dtype=r_dtype)
            elif r_dtype == 'dt':
                r_dtype = 'O'
                recons.index = np.array([Timestamp(label) for label in recons.index], dtype=r_dtype)
                df.index = np.array([Timestamp(label) for label in df.index], dtype=r_dtype)
            elif r_dtype == 'p':
                r_dtype = 'O'
                idx_list = to_datetime(recons.index)
                recons.index = np.array([Timestamp(label) for label in idx_list], dtype=r_dtype)
                df.index = np.array(list(map(Timestamp, df.index.to_timestamp())), dtype=r_dtype)
            else:
                r_dtype = type_map.get(r_dtype)
                recons.index = np.array(recons.index, dtype=r_dtype)
                df.index = np.array(df.index, dtype=r_dtype)
        if c_dtype:
            if c_dtype == 'u':
                c_dtype = 'O'
                recons.columns = np.array([_to_uni(label) for label in recons.columns], dtype=c_dtype)
                df.columns = np.array([_to_uni(label) for label in df.columns], dtype=c_dtype)
            elif c_dtype == 'dt':
                c_dtype = 'O'
                recons.columns = np.array([Timestamp(label) for label in recons.columns], dtype=c_dtype)
                df.columns = np.array([Timestamp(label) for label in df.columns], dtype=c_dtype)
            elif c_dtype == 'p':
                c_dtype = 'O'
                col_list = to_datetime(recons.columns)
                recons.columns = np.array([Timestamp(label) for label in col_list], dtype=c_dtype)
                col_list = df.columns.to_timestamp()
                df.columns = np.array([Timestamp(label) for label in col_list], dtype=c_dtype)
            else:
                c_dtype = type_map.get(c_dtype)
                recons.columns = np.array(recons.columns, dtype=c_dtype)
                df.columns = np.array(df.columns, dtype=c_dtype)
        tm.assert_frame_equal(df, recons, check_names=False, check_less_precise=True)
    N = 100
    chunksize = 1000
    for ncols in [4]:
        base = int((chunksize // ncols or 1) or 1)
        for nrows in [2, 10, N - 1, N, N + 1, N + 2, 2 * N - 2, 2 * N - 1, 2 * N, 2 * N + 1, 2 * N + 2, base - 1, base, base + 1]:
            _do_test(tm.makeCustomDataframe(nrows, ncols, r_idx_type='dt', c_idx_type='s'), 'dt', 's')
    for ncols in [4]:
        base = int((chunksize // ncols or 1) or 1)
        for nrows in [2, 10, N - 1, N, N + 1, N + 2, 2 * N - 2, 2 * N - 1, 2 * N, 2 * N + 1, 2 * N + 2, base - 1, base, base + 1]:
            _do_test(tm.makeCustomDataframe(nrows, ncols, r_idx_type='dt', c_idx_type='s'), 'dt', 's')
            pass
    for r_idx_type, c_idx_type in [('i', 'i'), ('s', 's'), ('u', 'dt'), ('p', 'p')]:
        for ncols in [1, 2, 3, 4]:
            base = int((chunksize // ncols or 1) or 1)
            for nrows in [2, 10, N - 1, N, N + 1, N + 2, 2 * N - 2, 2 * N - 1, 2 * N, 2 * N + 1, 2 * N + 2, base - 1, base, base + 1]:
                _do_test(tm.makeCustomDataframe(nrows, ncols, r_idx_type=r_idx_type, c_idx_type=c_idx_type), r_idx_type, c_idx_type)
    for ncols in [1, 2, 3, 4]:
        base = int((chunksize // ncols or 1) or 1)
        for nrows in [10, N - 2, N - 1, N, N + 1, N + 2, 2 * N - 2, 2 * N - 1, 2 * N, 2 * N + 1, 2 * N + 2, base - 1, base, base + 1]:
            _do_test(tm.makeCustomDataframe(nrows, ncols))
    for nrows in [10, N - 2, N - 1, N, N + 1, N + 2]:
        df = tm.makeCustomDataframe(nrows, 3)
        cols = list(df.columns)
        cols[:2] = ['dupe', 'dupe']
        cols[-2:] = ['dupe', 'dupe']
        ix = list(df.index)
        ix[:2] = ['rdupe', 'rdupe']
        ix[-2:] = ['rdupe', 'rdupe']
        df.index = ix
        df.columns = cols
        _do_test(df, dupe_col=True)
    _do_test(DataFrame(index=np.arange(10)))
    _do_test(tm.makeCustomDataframe(chunksize // 2 + 1, 2, r_idx_nlevels=2), rnlvl=2)
    for ncols in [2, 3, 4]:
        base = int(chunksize // ncols)
        for nrows in [10, N - 2, N - 1, N, N + 1, N + 2, 2 * N - 2, 2 * N - 1, 2 * N, 2 * N + 1, 2 * N + 2, base - 1, base, base + 1]:
            _do_test(tm.makeCustomDataframe(nrows, ncols, r_idx_nlevels=2), rnlvl=2)
            _do_test(tm.makeCustomDataframe(nrows, ncols, c_idx_nlevels=2), cnlvl=2)
            _do_test(tm.makeCustomDataframe(nrows, ncols, r_idx_nlevels=2, c_idx_nlevels=2), rnlvl=2, cnlvl=2)