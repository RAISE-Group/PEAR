def _can_reindex(self, indexer):
    """
        Check if we are allowing reindexing with this particular indexer.

        Parameters
        ----------
        indexer : an integer indexer

        Raises
        ------
        ValueError if its a duplicate axis
        """
    if not self.is_unique and len(indexer):
        raise ValueError('cannot reindex from a duplicate axis')