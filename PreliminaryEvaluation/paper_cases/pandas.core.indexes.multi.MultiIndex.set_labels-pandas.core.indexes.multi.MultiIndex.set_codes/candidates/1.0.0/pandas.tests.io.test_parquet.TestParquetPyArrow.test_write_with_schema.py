def test_write_with_schema(self, pa):
    import pyarrow
    df = pd.DataFrame({'x': [0, 1]})
    schema = pyarrow.schema([pyarrow.field('x', type=pyarrow.bool_())])
    out_df = df.astype(bool)
    check_round_trip(df, pa, write_kwargs={'schema': schema}, expected=out_df)