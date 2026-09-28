def _get_index_columns(self, tbl_name):
    from sqlalchemy.engine import reflection
    insp = reflection.Inspector.from_engine(self.conn)
    ixs = insp.get_indexes('test_index_saved')
    ixs = [i['column_names'] for i in ixs]
    return ixs