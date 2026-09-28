def test_file_handle_mmap(self):
    with open(self.csv1, 'rb') as f:
        reader = TextReader(f, memory_map=True, header=None)
        reader.read()