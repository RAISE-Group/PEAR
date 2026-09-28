def _encode(self, s):
    """
        Python 3 compatibility shim
        """
    return s.encode(self._encoding)