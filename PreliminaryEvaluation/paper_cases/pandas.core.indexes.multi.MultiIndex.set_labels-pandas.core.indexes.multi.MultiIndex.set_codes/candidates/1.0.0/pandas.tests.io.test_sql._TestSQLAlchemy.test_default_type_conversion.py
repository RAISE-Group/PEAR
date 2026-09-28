def test_default_type_conversion(self):
    df = sql.read_sql_table('types_test_data', self.conn)
    assert issubclass(df.FloatCol.dtype.type, np.floating)
    assert issubclass(df.IntCol.dtype.type, np.integer)
    assert issubclass(df.BoolCol.dtype.type, np.bool_)
    assert issubclass(df.IntColWithNull.dtype.type, np.floating)
    assert issubclass(df.BoolColWithNull.dtype.type, np.object)