@property
def is_mixed_type(self):
    self._consolidate_inplace()
    return len(self.blocks) > 1