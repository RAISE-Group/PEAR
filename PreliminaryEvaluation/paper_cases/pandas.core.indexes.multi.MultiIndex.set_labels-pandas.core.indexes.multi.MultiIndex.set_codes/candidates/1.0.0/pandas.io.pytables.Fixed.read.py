def read(self, where=None, columns=None, start: Optional[int]=None, stop: Optional[int]=None):
    raise NotImplementedError('cannot read on an abstract storer: subclasses should implement')