def test_read_columns(self, engine):
    df = pd.DataFrame({'string': list('abc'), 'int': list(range(1, 4))})
    expected = pd.DataFrame({'string': list('abc')})
    check_round_trip(df, engine, expected=expected, read_kwargs={'columns': ['string']})