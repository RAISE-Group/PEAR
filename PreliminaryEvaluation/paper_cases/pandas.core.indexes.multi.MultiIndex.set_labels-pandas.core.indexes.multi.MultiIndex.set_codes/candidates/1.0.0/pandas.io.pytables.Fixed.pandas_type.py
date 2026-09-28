@property
def pandas_type(self):
    return _ensure_decoded(getattr(self.group._v_attrs, 'pandas_type', None))