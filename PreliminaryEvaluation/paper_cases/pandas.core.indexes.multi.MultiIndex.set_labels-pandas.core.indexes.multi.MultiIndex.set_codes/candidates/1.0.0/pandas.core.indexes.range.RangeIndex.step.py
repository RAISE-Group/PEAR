@cache_readonly
def step(self):
    """
        The value of the `step` parameter (``1`` if this was not supplied).
        """
    return self._range.step