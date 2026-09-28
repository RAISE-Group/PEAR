def test_file_handle(self):
    with open(self.csv1, 'rb') as f:
        reader = TextReader(f)
        reader.read()