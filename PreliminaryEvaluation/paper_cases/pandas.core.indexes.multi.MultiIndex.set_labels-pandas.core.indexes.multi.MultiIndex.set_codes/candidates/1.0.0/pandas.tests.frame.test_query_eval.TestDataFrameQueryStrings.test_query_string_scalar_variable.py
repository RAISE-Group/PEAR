def test_query_string_scalar_variable(self, parser, engine):
    skip_if_no_pandas_parser(parser)
    df = pd.DataFrame({'Symbol': ['BUD US', 'BUD US', 'IBM US', 'IBM US'], 'Price': [109.7, 109.72, 183.3, 183.35]})
    e = df[df.Symbol == 'BUD US']
    symb = 'BUD US'
    r = df.query('Symbol == @symb', parser=parser, engine=engine)
    tm.assert_frame_equal(e, r)