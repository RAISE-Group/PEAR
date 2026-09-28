def _get_fill_indexer_searchsorted(self, target, method, limit=None):
    """
        Fallback pad/backfill get_indexer that works for monotonic decreasing
        indexes and non-monotonic targets.
        """
    if limit is not None:
        raise ValueError(f'limit argument for {repr(method)} method only well-defined if index and target are monotonic')
    side = 'left' if method == 'pad' else 'right'
    indexer = self.get_indexer(target)
    nonexact = indexer == -1
    indexer[nonexact] = self._searchsorted_monotonic(target[nonexact], side)
    if side == 'left':
        indexer[nonexact] -= 1
    else:
        indexer[indexer == len(self)] = -1
    return indexer