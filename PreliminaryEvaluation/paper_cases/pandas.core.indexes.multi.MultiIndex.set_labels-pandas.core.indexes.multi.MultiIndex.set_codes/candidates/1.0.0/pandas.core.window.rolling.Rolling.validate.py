def validate(self):
    super().validate()
    if (self.obj.empty or self.is_datetimelike) and isinstance(self.window, (str, ABCDateOffset, timedelta)):
        self._validate_monotonic()
        freq = self._validate_freq()
        if self.center:
            raise NotImplementedError('center is not implemented for datetimelike and offset based windows')
        self.win_freq = self.window
        self.window = freq.nanos
        self.win_type = 'freq'
        if self.min_periods is None:
            self.min_periods = 1
    elif isinstance(self.window, BaseIndexer):
        return
    elif not is_integer(self.window):
        raise ValueError('window must be an integer')
    elif self.window < 0:
        raise ValueError('window must be non-negative')
    if not self.is_datetimelike and self.closed is not None:
        raise ValueError('closed only implemented for datetimelike and offset based windows')