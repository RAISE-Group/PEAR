def _align_series(self, indexer, ser: ABCSeries, multiindex_indexer: bool=False):
    """
        Parameters
        ----------
        indexer : tuple, slice, scalar
            Indexer used to get the locations that will be set to `ser`.
        ser : pd.Series
            Values to assign to the locations specified by `indexer`.
        multiindex_indexer : boolean, optional
            Defaults to False. Should be set to True if `indexer` was from
            a `pd.MultiIndex`, to avoid unnecessary broadcasting.

        Returns
        -------
        `np.array` of `ser` broadcast to the appropriate shape for assignment
        to the locations selected by `indexer`
        """
    if isinstance(indexer, (slice, np.ndarray, list, Index)):
        indexer = tuple([indexer])
    if isinstance(indexer, tuple):

        def ravel(i):
            return i.ravel() if isinstance(i, np.ndarray) else i
        indexer = tuple(map(ravel, indexer))
        aligners = [not com.is_null_slice(idx) for idx in indexer]
        sum_aligners = sum(aligners)
        single_aligner = sum_aligners == 1
        is_frame = self.ndim == 2
        obj = self.obj
        if is_frame:
            single_aligner = single_aligner and aligners[0]
        if sum_aligners == self.ndim and all((is_sequence(_) for _ in indexer)):
            ser = ser.reindex(obj.axes[0][indexer[0]], copy=True)._values
            if len(indexer) > 1 and (not multiindex_indexer):
                len_indexer = len(indexer[1])
                ser = np.tile(ser, len_indexer).reshape(len_indexer, -1).T
            return ser
        for i, idx in enumerate(indexer):
            ax = obj.axes[i]
            if is_sequence(idx) or isinstance(idx, slice):
                if single_aligner and com.is_null_slice(idx):
                    continue
                new_ix = ax[idx]
                if not is_list_like_indexer(new_ix):
                    new_ix = Index([new_ix])
                else:
                    new_ix = Index(new_ix)
                if ser.index.equals(new_ix) or not len(new_ix):
                    return ser._values.copy()
                return ser.reindex(new_ix)._values
            elif single_aligner:
                ax = self.obj.axes[1]
                if ser.index.equals(ax) or not len(ax):
                    return ser._values.copy()
                return ser.reindex(ax)._values
    elif is_scalar(indexer):
        ax = self.obj._get_axis(1)
        if ser.index.equals(ax):
            return ser._values.copy()
        return ser.reindex(ax)._values
    raise ValueError('Incompatible indexer with Series')