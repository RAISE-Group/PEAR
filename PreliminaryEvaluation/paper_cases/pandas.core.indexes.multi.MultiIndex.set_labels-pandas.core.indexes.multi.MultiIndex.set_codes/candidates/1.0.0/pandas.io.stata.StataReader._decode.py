def _decode(self, s):
    s = s.partition(b'\x00')[0]
    try:
        return s.decode(self._encoding)
    except UnicodeDecodeError:
        encoding = self._encoding
        msg = f'\nOne or more strings in the dta file could not be decoded using {encoding}, and\nso the fallback encoding of latin-1 is being used.  This can happen when a file\nhas been incorrectly encoded by Stata or some other software. You should verify\nthe string values returned are correct.'
        warnings.warn(msg, UnicodeWarning)
        return s.decode('latin-1')