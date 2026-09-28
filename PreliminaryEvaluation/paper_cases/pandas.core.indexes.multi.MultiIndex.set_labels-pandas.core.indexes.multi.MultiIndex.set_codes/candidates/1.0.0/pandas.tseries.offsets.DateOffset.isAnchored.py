def isAnchored(self):
    warnings.warn('isAnchored is a deprecated, use is_anchored instead', FutureWarning, stacklevel=2)
    return self.is_anchored()