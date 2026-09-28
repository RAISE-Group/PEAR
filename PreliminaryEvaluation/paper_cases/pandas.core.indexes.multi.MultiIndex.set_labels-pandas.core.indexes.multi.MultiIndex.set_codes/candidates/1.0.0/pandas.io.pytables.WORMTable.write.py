def write(self, **kwargs):
    """ write in a format that we can search later on (but cannot append
               to): write out the indices and the values using _write_array
               (e.g. a CArray) create an indexing table so that we can search
        """
    raise NotImplementedError('WORMTable needs to implement write')