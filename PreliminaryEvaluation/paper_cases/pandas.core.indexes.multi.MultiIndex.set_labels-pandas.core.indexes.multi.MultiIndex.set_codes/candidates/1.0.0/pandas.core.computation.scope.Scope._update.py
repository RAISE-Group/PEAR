def _update(self, level: int):
    """
        Update the current scope by going back `level` levels.

        Parameters
        ----------
        level : int
        """
    sl = level + 1
    stack = inspect.stack()
    try:
        self._get_vars(stack[:sl], scopes=['locals'])
    finally:
        del stack[:], stack