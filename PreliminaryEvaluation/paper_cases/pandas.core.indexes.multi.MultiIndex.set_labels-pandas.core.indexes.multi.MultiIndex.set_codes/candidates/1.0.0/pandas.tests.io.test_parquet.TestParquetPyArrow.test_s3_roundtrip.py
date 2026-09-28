def test_s3_roundtrip(self, df_compat, s3_resource, pa):
    check_round_trip(df_compat, pa, path='s3://pandas-test/pyarrow.parquet')