def infer_axes(self):
    """ infer the axes of my storer
              return a boolean indicating if we have a valid storer or not """
    s = self.storable
    if s is None:
        return False
    self.get_attrs()
    return True