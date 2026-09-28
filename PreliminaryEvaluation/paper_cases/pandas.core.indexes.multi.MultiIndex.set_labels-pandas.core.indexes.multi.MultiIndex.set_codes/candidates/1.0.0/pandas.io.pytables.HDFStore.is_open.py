@property
def is_open(self) -> bool:
    """
        return a boolean indicating whether the file is open
        """
    if self._handle is None:
        return False
    return bool(self._handle.isopen)