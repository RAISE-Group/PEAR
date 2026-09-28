def queryables(self) -> Dict[str, Any]:
    """ return a dict of the kinds allowable columns for this object """
    axis_names = {0: 'index', 1: 'columns'}
    d1 = [(a.cname, a) for a in self.index_axes]
    d2 = [(axis_names[axis], None) for axis, values in self.non_index_axes]
    d3 = [(v.cname, v) for v in self.values_axes if v.name in set(self.data_columns)]
    return dict(d1 + d2 + d3)