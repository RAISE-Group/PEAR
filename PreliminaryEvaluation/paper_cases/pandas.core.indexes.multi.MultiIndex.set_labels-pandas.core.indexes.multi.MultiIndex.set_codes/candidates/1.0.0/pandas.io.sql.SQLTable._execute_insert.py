def _execute_insert(self, conn, keys, data_iter):
    """Execute SQL statement inserting data

        Parameters
        ----------
        conn : sqlalchemy.engine.Engine or sqlalchemy.engine.Connection
        keys : list of str
           Column names
        data_iter : generator of list
           Each item contains a list of values to be inserted
        """
    data = [dict(zip(keys, row)) for row in data_iter]
    conn.execute(self.table.insert(), data)