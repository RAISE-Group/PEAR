@staticmethod
def validate_dataframe(df: DataFrame):
    if not isinstance(df, DataFrame):
        raise ValueError('to_parquet only supports IO with DataFrames')
    if df.columns.inferred_type not in {'string', 'unicode', 'empty'}:
        raise ValueError('parquet must have string column names')
    valid_names = all((isinstance(name, str) for name in df.index.names if name is not None))
    if not valid_names:
        raise ValueError('Index level names must be strings')