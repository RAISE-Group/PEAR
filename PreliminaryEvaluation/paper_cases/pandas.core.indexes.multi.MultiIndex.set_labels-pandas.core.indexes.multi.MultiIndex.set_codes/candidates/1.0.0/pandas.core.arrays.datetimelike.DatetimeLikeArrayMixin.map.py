def map(self, mapper):
    from pandas import Index
    return Index(self).map(mapper).array