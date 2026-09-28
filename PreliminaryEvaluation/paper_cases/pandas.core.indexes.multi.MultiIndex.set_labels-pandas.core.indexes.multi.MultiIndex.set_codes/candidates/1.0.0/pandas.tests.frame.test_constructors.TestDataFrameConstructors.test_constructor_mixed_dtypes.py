def test_constructor_mixed_dtypes(self):

    def _make_mixed_dtypes_df(typ, ad=None):
        if typ == 'int':
            dtypes = MIXED_INT_DTYPES
            arrays = [np.array(np.random.rand(10), dtype=d) for d in dtypes]
        elif typ == 'float':
            dtypes = MIXED_FLOAT_DTYPES
            arrays = [np.array(np.random.randint(10, size=10), dtype=d) for d in dtypes]
        for d, a in zip(dtypes, arrays):
            assert a.dtype == d
        if ad is None:
            ad = dict()
        ad.update({d: a for d, a in zip(dtypes, arrays)})
        return DataFrame(ad)

    def _check_mixed_dtypes(df, dtypes=None):
        if dtypes is None:
            dtypes = MIXED_FLOAT_DTYPES + MIXED_INT_DTYPES
        for d in dtypes:
            if d in df:
                assert df.dtypes[d] == d
    df = _make_mixed_dtypes_df('float')
    _check_mixed_dtypes(df)
    df = _make_mixed_dtypes_df('float', dict(A=1, B='foo', C='bar'))
    _check_mixed_dtypes(df)
    df = _make_mixed_dtypes_df('int')
    _check_mixed_dtypes(df)