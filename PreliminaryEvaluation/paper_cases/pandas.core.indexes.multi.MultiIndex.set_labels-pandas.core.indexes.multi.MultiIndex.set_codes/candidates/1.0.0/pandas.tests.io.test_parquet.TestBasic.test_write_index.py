def test_write_index(self, engine):
    check_names = engine != 'fastparquet'
    df = pd.DataFrame({'A': [1, 2, 3]})
    check_round_trip(df, engine)
    indexes = [[2, 3, 4], pd.date_range('20130101', periods=3), list('abc'), [1, 3, 4]]
    for index in indexes:
        df.index = index
        check_round_trip(df, engine, check_names=check_names)
    df.index = [0, 1, 2]
    df.index.name = 'foo'
    check_round_trip(df, engine)