def _null_terminate(self, s, as_string=False):
    null_byte = '\x00'
    s += null_byte
    if not as_string:
        s = s.encode(self._encoding)
    return s