def read_sql(self, *args, **kwargs):
    raise ValueError('PandasSQL must be created with an SQLAlchemy connectable or sqlite connection')