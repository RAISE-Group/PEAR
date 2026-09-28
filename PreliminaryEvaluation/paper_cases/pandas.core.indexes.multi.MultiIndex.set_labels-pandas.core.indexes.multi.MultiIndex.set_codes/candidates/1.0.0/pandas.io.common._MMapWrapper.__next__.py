def __next__(self) -> str:
    newbytes = self.mmap.readline()
    newline = newbytes.decode('utf-8')
    if newline == '':
        raise StopIteration
    return newline