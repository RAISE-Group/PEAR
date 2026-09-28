def _execute_sql(self):
    iris_results = self.pandasSQL.execute('SELECT * FROM iris')
    row = iris_results.fetchone()
    tm.equalContents(row, [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'])