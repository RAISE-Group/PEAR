@property
def length(self):
    """
        Return an Index with entries denoting the length of each Interval in
        the IntervalArray.
        """
    try:
        return self.right - self.left
    except TypeError:
        msg = 'IntervalArray contains Intervals without defined length, e.g. Intervals with string endpoints'
        raise TypeError(msg)