def test_string_filename(self):
    reader = TextReader(self.csv1, header=None)
    reader.read()