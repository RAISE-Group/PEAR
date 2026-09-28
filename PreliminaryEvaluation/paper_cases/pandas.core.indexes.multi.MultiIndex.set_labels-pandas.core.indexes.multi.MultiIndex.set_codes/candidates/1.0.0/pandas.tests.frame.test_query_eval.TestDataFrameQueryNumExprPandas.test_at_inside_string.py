def test_at_inside_string(self):
    engine, parser = (self.engine, self.parser)
    skip_if_no_pandas_parser(parser)
    c = 1
    df = DataFrame({'a': ['a', 'a', 'b', 'b', '@c', '@c']})
    result = df.query('a == "@c"', engine=engine, parser=parser)
    expected = df[df.a == '@c']
    tm.assert_frame_equal(result, expected)