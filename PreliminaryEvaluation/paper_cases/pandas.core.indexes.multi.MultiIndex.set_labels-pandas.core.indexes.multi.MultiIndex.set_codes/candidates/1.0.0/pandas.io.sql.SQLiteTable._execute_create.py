def _execute_create(self):
    with self.pd_sql.run_transaction() as conn:
        for stmt in self.table:
            conn.execute(stmt)