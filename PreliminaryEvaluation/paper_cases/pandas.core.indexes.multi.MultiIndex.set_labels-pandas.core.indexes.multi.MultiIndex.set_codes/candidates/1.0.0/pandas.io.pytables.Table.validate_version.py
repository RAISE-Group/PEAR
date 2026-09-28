def validate_version(self, where=None):
    """ are we trying to operate on an old version? """
    if where is not None:
        if self.version[0] <= 0 and self.version[1] <= 10 and (self.version[2] < 1):
            ws = incompatibility_doc % '.'.join([str(x) for x in self.version])
            warnings.warn(ws, IncompatibilityWarning)