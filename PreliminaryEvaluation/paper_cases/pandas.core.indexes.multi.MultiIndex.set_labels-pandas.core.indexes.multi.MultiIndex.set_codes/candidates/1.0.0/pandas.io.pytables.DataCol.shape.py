@property
def shape(self):
    return getattr(self.data, 'shape', None)