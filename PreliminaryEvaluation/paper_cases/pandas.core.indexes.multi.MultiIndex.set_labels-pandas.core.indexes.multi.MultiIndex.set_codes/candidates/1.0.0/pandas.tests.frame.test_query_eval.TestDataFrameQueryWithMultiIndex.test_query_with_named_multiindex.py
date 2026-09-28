def test_query_with_named_multiindex(self, parser, engine):
    skip_if_no_pandas_parser(parser)
    a = np.random.choice(['red', 'green'], size=10)
    b = np.random.choice(['eggs', 'ham'], size=10)
    index = MultiIndex.from_arrays([a, b], names=['color', 'food'])
    df = DataFrame(np.random.randn(10, 2), index=index)
    ind = Series(df.index.get_level_values('color').values, index=index, name='color')
    res1 = df.query('color == "red"', parser=parser, engine=engine)
    res2 = df.query('"red" == color', parser=parser, engine=engine)
    exp = df[ind == 'red']
    tm.assert_frame_equal(res1, exp)
    tm.assert_frame_equal(res2, exp)
    res1 = df.query('color != "red"', parser=parser, engine=engine)
    res2 = df.query('"red" != color', parser=parser, engine=engine)
    exp = df[ind != 'red']
    tm.assert_frame_equal(res1, exp)
    tm.assert_frame_equal(res2, exp)
    res1 = df.query('color == ["red"]', parser=parser, engine=engine)
    res2 = df.query('["red"] == color', parser=parser, engine=engine)
    exp = df[ind.isin(['red'])]
    tm.assert_frame_equal(res1, exp)
    tm.assert_frame_equal(res2, exp)
    res1 = df.query('color != ["red"]', parser=parser, engine=engine)
    res2 = df.query('["red"] != color', parser=parser, engine=engine)
    exp = df[~ind.isin(['red'])]
    tm.assert_frame_equal(res1, exp)
    tm.assert_frame_equal(res2, exp)
    res1 = df.query('["red"] in color', parser=parser, engine=engine)
    res2 = df.query('"red" in color', parser=parser, engine=engine)
    exp = df[ind.isin(['red'])]
    tm.assert_frame_equal(res1, exp)
    tm.assert_frame_equal(res2, exp)
    res1 = df.query('["red"] not in color', parser=parser, engine=engine)
    res2 = df.query('"red" not in color', parser=parser, engine=engine)
    exp = df[~ind.isin(['red'])]
    tm.assert_frame_equal(res1, exp)
    tm.assert_frame_equal(res2, exp)