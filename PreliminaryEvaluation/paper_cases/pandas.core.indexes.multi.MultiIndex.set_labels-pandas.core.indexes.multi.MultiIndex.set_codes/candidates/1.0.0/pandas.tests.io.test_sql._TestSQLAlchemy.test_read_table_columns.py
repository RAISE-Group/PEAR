def test_read_table_columns(self):
    iris_frame = sql.read_sql_table('iris', con=self.conn, columns=['SepalLength', 'SepalLength'])
    tm.equalContents(iris_frame.columns.values, ['SepalLength', 'SepalLength'])