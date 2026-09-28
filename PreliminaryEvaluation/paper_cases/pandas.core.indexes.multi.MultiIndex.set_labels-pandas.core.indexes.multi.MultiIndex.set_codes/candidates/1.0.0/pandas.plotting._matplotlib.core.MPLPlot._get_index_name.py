def _get_index_name(self):
    if isinstance(self.data.index, ABCMultiIndex):
        name = self.data.index.names
        if com.any_not_none(*name):
            name = ','.join((pprint_thing(x) for x in name))
        else:
            name = None
    else:
        name = self.data.index.name
        if name is not None:
            name = pprint_thing(name)
    return name