def _make_reader(self, f):
    self.data = FixedWidthReader(f, self.colspecs, self.delimiter, self.comment, self.skiprows, self.infer_nrows)