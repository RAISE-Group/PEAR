def read(self, where=None, columns=None, start: Optional[int]=None, stop: Optional[int]=None):
    """ read the indices and the indexing array, calculate offset rows and
        return """
    raise NotImplementedError('WORMTable needs to implement read')