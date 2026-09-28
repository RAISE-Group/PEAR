def test_write_multiindex(self, pa):
    engine = pa
    df = pd.DataFrame({'A': [1, 2, 3]})
    index = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1)])
    df.index = index
    check_round_trip(df, engine)