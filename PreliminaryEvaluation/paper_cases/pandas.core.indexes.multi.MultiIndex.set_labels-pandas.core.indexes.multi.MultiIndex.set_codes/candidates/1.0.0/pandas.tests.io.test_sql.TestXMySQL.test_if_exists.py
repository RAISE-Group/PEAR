def test_if_exists(self):
    df_if_exists_1 = DataFrame({'col1': [1, 2], 'col2': ['A', 'B']})
    df_if_exists_2 = DataFrame({'col1': [3, 4, 5], 'col2': ['C', 'D', 'E']})
    table_name = 'table_if_exists'
    sql_select = f'SELECT * FROM {table_name}'

    def clean_up(test_table_to_drop):
        """
            Drops tables created from individual tests
            so no dependencies arise from sequential tests
            """
        self.drop_table(test_table_to_drop)
    with pytest.raises(ValueError, match='<insert message here>'):
        sql.to_sql(frame=df_if_exists_1, con=self.conn, name=table_name, if_exists='notvalidvalue')
    clean_up(table_name)
    sql.to_sql(frame=df_if_exists_1, con=self.conn, name=table_name, if_exists='fail', index=False)
    with pytest.raises(ValueError, match='<insert message here>'):
        sql.to_sql(frame=df_if_exists_1, con=self.conn, name=table_name, if_exists='fail')
    sql.to_sql(frame=df_if_exists_1, con=self.conn, name=table_name, if_exists='replace', index=False)
    assert tquery(sql_select, con=self.conn) == [(1, 'A'), (2, 'B')]
    sql.to_sql(frame=df_if_exists_2, con=self.conn, name=table_name, if_exists='replace', index=False)
    assert tquery(sql_select, con=self.conn) == [(3, 'C'), (4, 'D'), (5, 'E')]
    clean_up(table_name)
    sql.to_sql(frame=df_if_exists_1, con=self.conn, name=table_name, if_exists='fail', index=False)
    assert tquery(sql_select, con=self.conn) == [(1, 'A'), (2, 'B')]
    sql.to_sql(frame=df_if_exists_2, con=self.conn, name=table_name, if_exists='append', index=False)
    assert tquery(sql_select, con=self.conn) == [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
    clean_up(table_name)