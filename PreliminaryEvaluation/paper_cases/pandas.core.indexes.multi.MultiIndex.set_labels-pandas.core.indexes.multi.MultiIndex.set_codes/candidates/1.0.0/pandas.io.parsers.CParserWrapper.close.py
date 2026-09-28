def close(self):
    for f in self.handles:
        f.close()
    try:
        self._reader.close()
    except ValueError:
        pass