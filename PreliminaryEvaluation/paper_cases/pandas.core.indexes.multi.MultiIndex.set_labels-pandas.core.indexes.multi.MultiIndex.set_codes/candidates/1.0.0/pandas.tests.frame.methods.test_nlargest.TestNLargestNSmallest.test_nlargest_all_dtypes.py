def test_nlargest_all_dtypes(self, df_main_dtypes):
    df = df_main_dtypes
    df.nsmallest(2, list(set(df) - {'category_string', 'string'}))
    df.nlargest(2, list(set(df) - {'category_string', 'string'}))