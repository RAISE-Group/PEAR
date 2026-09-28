def test_write_ignoring_index(self, engine):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['q', 'r', 's']})
    write_kwargs = {'compression': None, 'index': False}
    expected = df.reset_index(drop=True)
    check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['q', 'r', 's']}, index=['zyx', 'wvu', 'tsr'])
    check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
    arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
    df = pd.DataFrame({'one': list(range(8)), 'two': [-i for i in range(8)]}, index=arrays)
    expected = df.reset_index(drop=True)
    check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)