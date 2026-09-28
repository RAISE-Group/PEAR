@property
def root(self):
    """ return the root node """
    self._check_if_open()
    return self._handle.root