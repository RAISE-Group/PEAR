def test_execute_sql(self):
    iris_results = sql.execute('SELECT * FROM iris', con=self.conn)
    row = iris_results.fetchone()
    tm.equalContents(row, [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'])