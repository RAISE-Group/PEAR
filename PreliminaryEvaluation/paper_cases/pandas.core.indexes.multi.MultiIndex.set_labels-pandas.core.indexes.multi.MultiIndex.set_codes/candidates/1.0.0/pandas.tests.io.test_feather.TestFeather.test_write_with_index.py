def test_write_with_index(self):
    df = pd.DataFrame({'A': [1, 2, 3]})
    self.check_round_trip(df)
    for index in [[2, 3, 4], pd.date_range('20130101', periods=3), list('abc'), [1, 3, 4], pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1)])]:
        df.index = index
        self.check_error_on_write(df, ValueError)
    df.index = [0, 1, 2]
    df.index.name = 'foo'
    self.check_error_on_write(df, ValueError)
    df.index = [0, 1, 2]
    df.columns = pd.MultiIndex.from_tuples([('a', 1)])
    self.check_error_on_write(df, ValueError)