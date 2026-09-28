def _set_grouper(self, obj: FrameOrSeries, sort: bool=False):
    """
        given an object and the specifications, setup the internal grouper
        for this particular specification

        Parameters
        ----------
        obj : Series or DataFrame
        sort : bool, default False
            whether the resulting grouper should be sorted
        """
    assert obj is not None
    if self.key is not None and self.level is not None:
        raise ValueError('The Grouper cannot specify both a key and a level!')
    if self._grouper is None:
        self._grouper = self.grouper
    if self.key is not None:
        key = self.key
        if getattr(self.grouper, 'name', None) == key and isinstance(obj, ABCSeries):
            ax = self._grouper.take(obj.index)
        else:
            if key not in obj._info_axis:
                raise KeyError(f'The grouper name {key} is not found')
            ax = Index(obj[key], name=key)
    else:
        ax = obj._get_axis(self.axis)
        if self.level is not None:
            level = self.level
            if isinstance(ax, MultiIndex):
                level = ax._get_level_number(level)
                ax = Index(ax._get_level_values(level), name=ax.names[level])
            elif level not in (0, ax.name):
                raise ValueError(f'The level {level} is not valid')
    if (self.sort or sort) and (not ax.is_monotonic):
        indexer = self.indexer = ax.argsort(kind='mergesort')
        ax = ax.take(indexer)
        obj = obj.take(indexer, axis=self.axis)
    self.obj = obj
    self.grouper = ax
    return self.grouper