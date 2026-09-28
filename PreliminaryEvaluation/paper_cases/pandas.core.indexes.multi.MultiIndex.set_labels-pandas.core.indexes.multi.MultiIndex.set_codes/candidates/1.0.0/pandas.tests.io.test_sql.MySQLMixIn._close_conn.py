def _close_conn(self):
    from pymysql.err import Error
    try:
        self.conn.close()
    except Error:
        pass