def test_connectable_issue_example(self):

    def foo(connection):
        query = 'SELECT test_foo_data FROM test_foo_data'
        return sql.read_sql_query(query, con=connection)

    def bar(connection, data):
        data.to_sql(name='test_foo_data', con=connection, if_exists='append')

    def main(connectable):
        with connectable.connect() as conn:
            with conn.begin():
                foo_data = conn.run_callable(foo)
                conn.run_callable(bar, foo_data)
    DataFrame({'test_foo_data': [0, 1, 2]}).to_sql('test_foo_data', self.conn)
    main(self.conn)