def _update_map(self, tag):
    """Update map location for tag with file position"""
    self._map[tag] = self._file.tell()