def _read_bytes(self, offset, length):
    if self._cached_page is None:
        self._path_or_buf.seek(offset)
        buf = self._path_or_buf.read(length)
        if len(buf) < length:
            self.close()
            msg = f'Unable to read {length:d} bytes from file position {offset:d}.'
            raise ValueError(msg)
        return buf
    else:
        if offset + length > len(self._cached_page):
            self.close()
            raise ValueError('The cached page is too small.')
        return self._cached_page[offset:offset + length]