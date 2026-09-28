def get_table(self, table_name, schema=None):
    schema = schema or self.meta.schema
    if schema:
        tbl = self.meta.tables.get('.'.join([schema, table_name]))
    else:
        tbl = self.meta.tables.get(table_name)
    from sqlalchemy import Numeric
    for column in tbl.columns:
        if isinstance(column.type, Numeric):
            column.type.asdecimal = False
    return tbl