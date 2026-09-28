def _get_all_tables(self):
    meta = sqlalchemy.schema.MetaData(bind=self.conn)
    meta.reflect()
    table_list = meta.tables.keys()
    return table_list