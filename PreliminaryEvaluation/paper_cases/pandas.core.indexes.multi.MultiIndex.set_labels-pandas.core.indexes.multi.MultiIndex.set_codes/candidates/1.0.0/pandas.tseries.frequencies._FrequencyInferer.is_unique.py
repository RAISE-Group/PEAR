@cache_readonly
def is_unique(self) -> bool:
    return len(self.deltas) == 1