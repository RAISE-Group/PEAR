def test_str_list_query_method(self, parser, engine):
    df = DataFrame(np.random.randn(10, 1), columns=['b'])
    df['strings'] = Series(list('aabbccddee'))
    expect = df[df.strings.isin(['a', 'b'])]
    if parser != 'pandas':
        col = 'strings'
        lst = '["a", "b"]'
        lhs = [col] * 2 + [lst] * 2
        rhs = lhs[::-1]
        eq, ne = ('==', '!=')
        ops = 2 * ([eq] + [ne])
        for lhs, op, rhs in zip(lhs, ops, rhs):
            ex = '{lhs} {op} {rhs}'.format(lhs=lhs, op=op, rhs=rhs)
            with pytest.raises(NotImplementedError):
                df.query(ex, engine=engine, parser=parser)
    else:
        res = df.query('strings == ["a", "b"]', engine=engine, parser=parser)
        tm.assert_frame_equal(res, expect)
        res = df.query('["a", "b"] == strings', engine=engine, parser=parser)
        tm.assert_frame_equal(res, expect)
        expect = df[~df.strings.isin(['a', 'b'])]
        res = df.query('strings != ["a", "b"]', engine=engine, parser=parser)
        tm.assert_frame_equal(res, expect)
        res = df.query('["a", "b"] != strings', engine=engine, parser=parser)
        tm.assert_frame_equal(res, expect)