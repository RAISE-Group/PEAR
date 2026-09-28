def test_query_with_string_columns(self, parser, engine):
    df = DataFrame({'a': list('aaaabbbbcccc'), 'b': list('aabbccddeeff'), 'c': np.random.randint(5, size=12), 'd': np.random.randint(9, size=12)})
    if parser == 'pandas':
        res = df.query('a in b', parser=parser, engine=engine)
        expec = df[df.a.isin(df.b)]
        tm.assert_frame_equal(res, expec)
        res = df.query('a in b and c < d', parser=parser, engine=engine)
        expec = df[df.a.isin(df.b) & (df.c < df.d)]
        tm.assert_frame_equal(res, expec)
    else:
        with pytest.raises(NotImplementedError):
            df.query('a in b', parser=parser, engine=engine)
        with pytest.raises(NotImplementedError):
            df.query('a in b and c < d', parser=parser, engine=engine)