def test_metadata_propagation(self):
    o = self._construct(shape=3)
    o.name = 'foo'
    o2 = self._construct(shape=3)
    o2.name = 'bar'
    for op in ['__add__', '__sub__', '__truediv__', '__mul__']:
        result = getattr(o, op)(1)
        self.check_metadata(o, result)
    for op in ['__add__', '__sub__', '__truediv__', '__mul__']:
        result = getattr(o, op)(o)
        self.check_metadata(o, result)
    for op in ['__eq__', '__le__', '__ge__']:
        v1 = getattr(o, op)(o)
        self.check_metadata(o, v1)
        self.check_metadata(o, v1 & v1)
        self.check_metadata(o, v1 | v1)
    result = o.combine_first(o2)
    self.check_metadata(o, result)
    result = o + o2
    self.check_metadata(result)
    for op in ['__eq__', '__le__', '__ge__']:
        v1 = getattr(o, op)(o)
        v2 = getattr(o, op)(o2)
        self.check_metadata(v2)
        self.check_metadata(v1 & v2)
        self.check_metadata(v1 | v2)