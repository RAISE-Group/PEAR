def _buffered_line(self):
    """
        Return a line from buffer, filling buffer if required.
        """
    if len(self.buf) > 0:
        return self.buf[0]
    else:
        return self._next_line()