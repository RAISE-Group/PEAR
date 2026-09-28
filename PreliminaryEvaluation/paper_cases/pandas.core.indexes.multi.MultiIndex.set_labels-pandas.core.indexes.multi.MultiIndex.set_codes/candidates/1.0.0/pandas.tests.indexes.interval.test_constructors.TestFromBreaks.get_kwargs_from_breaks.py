def get_kwargs_from_breaks(self, breaks, closed='right'):
    """
        converts intervals in breaks format to a dictionary of kwargs to
        specific to the format expected by IntervalIndex.from_breaks
        """
    return {'breaks': breaks}