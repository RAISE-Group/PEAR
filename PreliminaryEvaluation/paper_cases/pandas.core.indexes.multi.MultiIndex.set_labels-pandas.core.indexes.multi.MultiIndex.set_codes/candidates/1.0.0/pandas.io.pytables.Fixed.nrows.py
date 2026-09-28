@property
def nrows(self):
    return getattr(self.storable, 'nrows', None)