def test_illegal_names(self):
    df = DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
    msg = 'Empty table or column name specified'
    with pytest.raises(ValueError, match=msg):
        df.to_sql('', self.conn)
    for ndx, weird_name in enumerate(['test_weird_name]', 'test_weird_name[', 'test_weird_name`', 'test_weird_name"', "test_weird_name'", '_b.test_weird_name_01-30', '"_b.test_weird_name_01-30"', '99beginswithnumber', '12345', 'é']):
        df.to_sql(weird_name, self.conn)
        sql.table_exists(weird_name, self.conn)
        df2 = DataFrame([[1, 2], [3, 4]], columns=['a', weird_name])
        c_tbl = f'test_weird_col_name{ndx:d}'
        df2.to_sql(c_tbl, self.conn)
        sql.table_exists(c_tbl, self.conn)