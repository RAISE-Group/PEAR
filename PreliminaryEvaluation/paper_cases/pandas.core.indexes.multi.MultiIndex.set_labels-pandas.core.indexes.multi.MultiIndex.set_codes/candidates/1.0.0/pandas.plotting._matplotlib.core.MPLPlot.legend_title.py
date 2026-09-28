@property
def legend_title(self):
    if not isinstance(self.data.columns, ABCMultiIndex):
        name = self.data.columns.name
        if name is not None:
            name = pprint_thing(name)
        return name
    else:
        stringified = map(pprint_thing, self.data.columns.names)
        return ','.join(stringified)