def delete(self, where=None, start: Optional[int]=None, stop: Optional[int]=None):
    """
        support fully deleting the node in its entirety (only) - where
        specification must be None
        """
    if com.all_none(where, start, stop):
        self._handle.remove_node(self.group, recursive=True)
        return None
    raise TypeError('cannot delete on an abstract storer')