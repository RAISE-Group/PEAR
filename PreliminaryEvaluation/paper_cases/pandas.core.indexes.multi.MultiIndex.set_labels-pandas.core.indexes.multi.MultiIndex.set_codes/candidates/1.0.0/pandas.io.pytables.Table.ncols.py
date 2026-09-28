@property
def ncols(self) -> int:
    """ the number of total columns in the values axes """
    return sum((len(a.values) for a in self.values_axes))