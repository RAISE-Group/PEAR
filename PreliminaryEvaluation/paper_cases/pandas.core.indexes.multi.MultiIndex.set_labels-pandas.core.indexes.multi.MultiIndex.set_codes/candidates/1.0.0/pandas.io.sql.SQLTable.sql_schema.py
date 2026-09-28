def sql_schema(self):
    from sqlalchemy.schema import CreateTable
    return str(CreateTable(self.table).compile(self.pd_sql.connectable))