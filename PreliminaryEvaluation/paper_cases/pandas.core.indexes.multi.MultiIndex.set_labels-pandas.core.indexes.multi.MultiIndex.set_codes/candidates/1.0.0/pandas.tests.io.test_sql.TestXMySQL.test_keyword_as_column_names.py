def test_keyword_as_column_names(self):
    df = DataFrame({'From': np.ones(5)})
    sql.to_sql(df, con=self.conn, name='testkeywords', if_exists='replace', index=False)