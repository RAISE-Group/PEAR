def generate(self, where):
    """ where can be a : dict,list,tuple,string """
    if where is None:
        return None
    q = self.table.queryables()
    try:
        return PyTablesExpr(where, queryables=q, encoding=self.table.encoding)
    except NameError:
        qkeys = ','.join(q.keys())
        raise ValueError(f"The passed where expression: {where}\n            contains an invalid variable reference\n            all of the variable references must be a reference to\n            an axis (e.g. 'index' or 'columns'), or a data_column\n            The currently defined references are: {qkeys}\n")