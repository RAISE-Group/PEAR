def _count_rows(self, table_name):
    result = self._get_exec().execute(f'SELECT count(*) AS count_1 FROM {table_name}').fetchone()
    return result[0]