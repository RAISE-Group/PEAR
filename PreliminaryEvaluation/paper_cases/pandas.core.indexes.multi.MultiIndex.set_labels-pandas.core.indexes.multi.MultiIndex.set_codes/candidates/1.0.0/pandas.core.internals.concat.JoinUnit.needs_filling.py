@cache_readonly
def needs_filling(self):
    for indexer in self.indexers.values():
        if (indexer == -1).any():
            return True
    return False