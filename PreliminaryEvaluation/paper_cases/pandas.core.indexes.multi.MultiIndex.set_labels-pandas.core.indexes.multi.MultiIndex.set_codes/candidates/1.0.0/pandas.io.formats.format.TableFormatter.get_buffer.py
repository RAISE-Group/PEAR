@contextmanager
def get_buffer(self, buf: Optional[FilePathOrBuffer[str]], encoding: Optional[str]=None):
    """
        Context manager to open, yield and close buffer for filenames or Path-like
        objects, otherwise yield buf unchanged.
        """
    if buf is not None:
        buf = stringify_path(buf)
    else:
        buf = StringIO()
    if encoding is None:
        encoding = 'utf-8'
    elif not isinstance(buf, str):
        raise ValueError('buf is not a file name and encoding is specified.')
    if hasattr(buf, 'write'):
        yield buf
    elif isinstance(buf, str):
        with open(buf, 'w', encoding=encoding, newline='') as f:
            yield f
    else:
        raise TypeError('buf is not a file name and it has no write method')