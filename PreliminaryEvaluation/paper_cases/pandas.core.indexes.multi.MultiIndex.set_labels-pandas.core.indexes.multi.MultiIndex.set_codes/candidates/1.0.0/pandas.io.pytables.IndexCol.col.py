@property
def col(self):
    """ return my current col description """
    return getattr(self.description, self.cname, None)