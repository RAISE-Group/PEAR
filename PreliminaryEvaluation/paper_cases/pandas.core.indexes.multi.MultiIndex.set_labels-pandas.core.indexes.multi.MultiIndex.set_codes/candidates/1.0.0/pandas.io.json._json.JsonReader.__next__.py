def __next__(self):
    lines = list(islice(self.data, self.chunksize))
    if lines:
        lines_json = self._combine_lines(lines)
        obj = self._get_object_parser(lines_json)
        obj.index = range(self.nrows_seen, self.nrows_seen + len(obj))
        self.nrows_seen += len(obj)
        return obj
    self.close()
    raise StopIteration