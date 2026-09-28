def test_s3_roundtrip(self, df_compat, s3_resource, fp):
    check_round_trip(df_compat, fp, path='s3://pandas-test/fastparquet.parquet')