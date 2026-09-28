@property
def storable(self):
    return getattr(self.group, 'table', None)