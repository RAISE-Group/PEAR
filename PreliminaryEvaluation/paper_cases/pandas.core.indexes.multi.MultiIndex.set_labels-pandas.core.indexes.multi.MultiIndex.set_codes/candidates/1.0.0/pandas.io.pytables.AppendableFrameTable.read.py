def read(self, where=None, columns=None, start: Optional[int]=None, stop: Optional[int]=None):
    self.validate_version(where)
    if not self.infer_axes():
        return None
    result = self._read_axes(where=where, start=start, stop=stop)
    info = self.info.get(self.non_index_axes[0][0], dict()) if len(self.non_index_axes) else dict()
    inds = [i for i, ax in enumerate(self.axes) if ax is self.index_axes[0]]
    assert len(inds) == 1
    ind = inds[0]
    index = result[ind][0]
    frames = []
    for i, a in enumerate(self.axes):
        if a not in self.values_axes:
            continue
        index_vals, cvalues = result[i]
        if info.get('type') == 'MultiIndex':
            cols = MultiIndex.from_tuples(index_vals)
        else:
            cols = Index(index_vals)
        names = info.get('names')
        if names is not None:
            cols.set_names(names, inplace=True)
        if self.is_transposed:
            values = cvalues
            index_ = cols
            cols_ = Index(index, name=getattr(index, 'name', None))
        else:
            values = cvalues.T
            index_ = Index(index, name=getattr(index, 'name', None))
            cols_ = cols
        if values.ndim == 1 and isinstance(values, np.ndarray):
            values = values.reshape((1, values.shape[0]))
        if isinstance(values, np.ndarray):
            df = DataFrame(values.T, columns=cols_, index=index_)
        elif isinstance(values, Index):
            df = DataFrame(values, columns=cols_, index=index_)
        else:
            df = DataFrame([values], columns=cols_, index=index_)
        assert (df.dtypes == values.dtype).all(), (df.dtypes, values.dtype)
        frames.append(df)
    if len(frames) == 1:
        df = frames[0]
    else:
        df = concat(frames, axis=1)
    selection = Selection(self, where=where, start=start, stop=stop)
    df = self.process_axes(df, selection=selection, columns=columns)
    return df