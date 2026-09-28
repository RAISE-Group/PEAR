def __next__(self):
    try:
        return self.get_chunk()
    except StopIteration:
        self.close()
        raise