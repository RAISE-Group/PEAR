def __exit__(self, exc_type, exc_value, traceback):
    """ exit context manager """
    self.close()