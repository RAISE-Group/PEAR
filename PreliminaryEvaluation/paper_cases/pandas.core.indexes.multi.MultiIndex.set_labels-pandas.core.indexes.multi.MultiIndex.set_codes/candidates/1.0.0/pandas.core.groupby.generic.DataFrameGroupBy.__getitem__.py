def __getitem__(self, key):
    if isinstance(key, tuple) and len(key) > 1:
        warnings.warn('Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.', FutureWarning, stacklevel=2)
    return super().__getitem__(key)