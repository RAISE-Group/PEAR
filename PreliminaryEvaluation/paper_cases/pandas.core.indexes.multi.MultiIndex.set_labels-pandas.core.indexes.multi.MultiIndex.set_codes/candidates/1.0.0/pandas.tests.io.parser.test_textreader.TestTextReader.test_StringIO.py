def test_StringIO(self):
    with open(self.csv1, 'rb') as f:
        text = f.read()
    src = BytesIO(text)
    reader = TextReader(src, header=None)
    reader.read()