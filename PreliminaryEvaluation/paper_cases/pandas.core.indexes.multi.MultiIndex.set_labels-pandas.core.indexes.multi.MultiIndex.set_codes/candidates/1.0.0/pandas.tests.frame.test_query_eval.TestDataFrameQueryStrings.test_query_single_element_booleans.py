def test_query_single_element_booleans(self, parser, engine):
    columns = ('bid', 'bidsize', 'ask', 'asksize')
    data = np.random.randint(2, size=(1, len(columns))).astype(bool)
    df = DataFrame(data, columns=columns)
    res = df.query('bid & ask', engine=engine, parser=parser)
    expected = df[df.bid & df.ask]
    tm.assert_frame_equal(res, expected)