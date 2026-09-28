def check_metadata(self, x, y=None):
    for m in x._metadata:
        v = getattr(x, m, None)
        if y is None:
            assert v is None
        else:
            assert v == getattr(y, m, None)