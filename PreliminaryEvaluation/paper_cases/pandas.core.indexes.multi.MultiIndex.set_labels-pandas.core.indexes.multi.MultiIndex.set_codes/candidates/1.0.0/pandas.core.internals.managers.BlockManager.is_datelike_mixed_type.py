@property
def is_datelike_mixed_type(self):
    self._consolidate_inplace()
    return any((block.is_datelike for block in self.blocks))