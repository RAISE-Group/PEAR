@property
def is_indexed(self) -> bool:
    """ return whether I am an indexed column """
    if not hasattr(self.table, 'cols'):
        return False
    return getattr(self.table.cols, self.cname).is_indexed