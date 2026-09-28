def read_metadata(self, key: str):
    """ return the meta data array for this key """
    if getattr(getattr(self.group, 'meta', None), key, None) is not None:
        return self.parent.select(self._get_metadata_path(key))
    return None