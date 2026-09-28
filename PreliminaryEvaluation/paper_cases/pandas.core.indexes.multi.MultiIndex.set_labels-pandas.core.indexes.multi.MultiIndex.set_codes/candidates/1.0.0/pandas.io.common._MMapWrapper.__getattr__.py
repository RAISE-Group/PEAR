def __getattr__(self, name: str):
    return getattr(self.mmap, name)