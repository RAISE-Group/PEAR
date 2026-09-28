def _get_metadata_path(self, key: str) -> str:
    """ return the metadata pathname for this key """
    group = self.group._v_pathname
    return f'{group}/meta/{key}/meta'