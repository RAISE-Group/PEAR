def test_onecolumn_of_integer(self):
    mono_df = DataFrame([1, 2], columns=['c0'])
    sql.to_sql(mono_df, con=self.conn, name='mono_df', index=False)
    con_x = self.conn
    the_sum = sum((my_c0[0] for my_c0 in con_x.execute('select * from mono_df')))
    assert the_sum == 3
    result = sql.read_sql('select * from mono_df', con_x)
    tm.assert_frame_equal(result, mono_df)