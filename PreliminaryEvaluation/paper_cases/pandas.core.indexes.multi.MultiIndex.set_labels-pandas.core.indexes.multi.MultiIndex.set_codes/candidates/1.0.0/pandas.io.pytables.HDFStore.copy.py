def copy(self, file, mode='w', propindexes: bool=True, keys=None, complib=None, complevel: Optional[int]=None, fletcher32: bool=False, overwrite=True):
    """
        Copy the existing store to a new file, updating in place.

        Parameters
        ----------
        propindexes: bool, default True
            Restore indexes in copied file.
        keys       : list of keys to include in the copy (defaults to all)
        overwrite  : overwrite (remove and replace) existing nodes in the
            new store (default is True)
        mode, complib, complevel, fletcher32 same as in HDFStore.__init__

        Returns
        -------
        open file handle of the new store
        """
    new_store = HDFStore(file, mode=mode, complib=complib, complevel=complevel, fletcher32=fletcher32)
    if keys is None:
        keys = list(self.keys())
    if not isinstance(keys, (tuple, list)):
        keys = [keys]
    for k in keys:
        s = self.get_storer(k)
        if s is not None:
            if k in new_store:
                if overwrite:
                    new_store.remove(k)
            data = self.select(k)
            if isinstance(s, Table):
                index: Union[bool, List[str]] = False
                if propindexes:
                    index = [a.name for a in s.axes if a.is_indexed]
                new_store.append(k, data, index=index, data_columns=getattr(s, 'data_columns', None), encoding=s.encoding)
            else:
                new_store.put(k, data, encoding=s.encoding)
    return new_store