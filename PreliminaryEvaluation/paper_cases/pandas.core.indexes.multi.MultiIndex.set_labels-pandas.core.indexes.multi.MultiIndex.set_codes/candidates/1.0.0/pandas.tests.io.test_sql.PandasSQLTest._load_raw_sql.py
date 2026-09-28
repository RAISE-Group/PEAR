def _load_raw_sql(self):
    self.drop_table('types_test_data')
    self._get_exec().execute(SQL_STRINGS['create_test_types'][self.flavor])
    ins = SQL_STRINGS['insert_test_types'][self.flavor]
    data = [{'TextCol': 'first', 'DateCol': '2000-01-03 00:00:00', 'DateColWithTz': '2000-01-01 00:00:00-08:00', 'IntDateCol': 535852800, 'IntDateOnlyCol': 20101010, 'FloatCol': 10.1, 'IntCol': 1, 'BoolCol': False, 'IntColWithNull': 1, 'BoolColWithNull': False}, {'TextCol': 'first', 'DateCol': '2000-01-04 00:00:00', 'DateColWithTz': '2000-06-01 00:00:00-07:00', 'IntDateCol': 1356998400, 'IntDateOnlyCol': 20101212, 'FloatCol': 10.1, 'IntCol': 1, 'BoolCol': False, 'IntColWithNull': None, 'BoolColWithNull': None}]
    for d in data:
        self._get_exec().execute(ins['query'], [d[field] for field in ins['fields']])