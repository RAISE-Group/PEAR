@property
def axes(self):
    return itertools.chain(self.index_axes, self.values_axes)