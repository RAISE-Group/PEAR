def test_safe_names_warning(self):
    df = DataFrame([[1, 2], [3, 4]], columns=['a', 'b '])
    with tm.assert_produces_warning():
        sql.to_sql(df, 'test_frame3_legacy', self.conn, index=False)