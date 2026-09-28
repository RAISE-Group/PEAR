def _maybe_make_multi_index_columns(self, columns, col_names=None):
    if _is_potential_multi_index(columns):
        columns = MultiIndex.from_tuples(columns, names=col_names)
    return columns