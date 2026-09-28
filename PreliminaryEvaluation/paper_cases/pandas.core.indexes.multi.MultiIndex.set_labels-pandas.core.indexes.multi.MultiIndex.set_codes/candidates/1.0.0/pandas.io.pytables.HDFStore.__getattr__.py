def __getattr__(self, name: str):
    """ allow attribute access to get stores """
    try:
        return self.get(name)
    except (KeyError, ClosedFileError):
        pass
    raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")