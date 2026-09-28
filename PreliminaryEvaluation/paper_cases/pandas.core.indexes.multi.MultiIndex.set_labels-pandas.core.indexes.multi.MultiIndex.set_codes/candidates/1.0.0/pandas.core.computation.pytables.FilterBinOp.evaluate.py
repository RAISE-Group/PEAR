def evaluate(self):
    if not self.is_valid:
        raise ValueError(f'query term is not valid [{self}]')
    rhs = self.conform(self.rhs)
    values = list(rhs)
    if self.is_in_table:
        if self.op in ['==', '!='] and len(values) > self._max_selectors:
            filter_op = self.generate_filter_op()
            self.filter = (self.lhs, filter_op, pd.Index(values))
            return self
        return None
    if self.op in ['==', '!=']:
        filter_op = self.generate_filter_op()
        self.filter = (self.lhs, filter_op, pd.Index(values))
    else:
        raise TypeError(f'passing a filterable condition to a non-table indexer [{self}]')
    return self