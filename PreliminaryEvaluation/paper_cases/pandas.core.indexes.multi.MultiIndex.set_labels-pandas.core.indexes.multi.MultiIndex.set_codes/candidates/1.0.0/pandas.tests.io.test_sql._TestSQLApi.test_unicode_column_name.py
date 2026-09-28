def test_unicode_column_name(self):
    df = DataFrame([[1, 2], [3, 4]], columns=['é', 'b'])
    df.to_sql('test_unicode', self.conn, index=False)