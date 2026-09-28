def test_columns_dtypes(self, engine):
    df = pd.DataFrame({'string': list('abc'), 'int': list(range(1, 4))})
    df.columns = ['foo', 'bar']
    check_round_trip(df, engine)