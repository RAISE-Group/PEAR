def _slice(self, slicer):
    """ return a slice of my values """
    if isinstance(slicer, tuple) and len(slicer) == 2:
        if not com.is_null_slice(slicer[0]):
            raise AssertionError('invalid slicing for a 1-ndim categorical')
        slicer = slicer[1]
    return self.values[slicer]