def _create_join_index(self, index: Index, other_index: Index, indexer, other_indexer, how: str='left'):
    """
        Create a join index by rearranging one index to match another

        Parameters
        ----------
        index: Index being rearranged
        other_index: Index used to supply values not found in index
        indexer: how to rearrange index
        how: replacement is only necessary if indexer based on other_index

        Returns
        -------
        join_index
        """
    if self.how in (how, 'outer') and (not isinstance(other_index, MultiIndex)):
        mask = indexer == -1
        if np.any(mask):
            fill_value = na_value_for_dtype(index.dtype, compat=False)
            index = index.append(Index([fill_value]))
    return index.take(indexer)