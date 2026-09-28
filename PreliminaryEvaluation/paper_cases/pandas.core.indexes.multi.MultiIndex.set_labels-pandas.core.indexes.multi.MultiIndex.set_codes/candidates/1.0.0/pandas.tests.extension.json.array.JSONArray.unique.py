def unique(self):
    return type(self)([dict(x) for x in list({tuple(d.items()) for d in self.data})])