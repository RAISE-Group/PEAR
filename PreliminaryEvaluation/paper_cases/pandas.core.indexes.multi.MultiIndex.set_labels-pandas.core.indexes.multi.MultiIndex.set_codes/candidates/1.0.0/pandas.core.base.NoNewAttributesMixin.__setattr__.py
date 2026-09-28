def __setattr__(self, key, value):
    if getattr(self, '__frozen', False) and (not (key == '_cache' or key in type(self).__dict__ or getattr(self, key, None) is not None)):
        raise AttributeError(f"You cannot add any new attribute '{key}'")
    object.__setattr__(self, key, value)