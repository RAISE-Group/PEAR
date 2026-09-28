@contextmanager
def use(self, key, value):
    """
        Temporarily set a parameter value using the with statement.
        Aliasing allowed.
        """
    old_value = self[key]
    try:
        self[key] = value
        yield self
    finally:
        self[key] = old_value