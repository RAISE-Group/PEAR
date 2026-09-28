@property
def _engine_type(self):
    return {np.int8: libindex.Int8Engine, np.int16: libindex.Int16Engine, np.int32: libindex.Int32Engine, np.int64: libindex.Int64Engine}[self.codes.dtype.type]