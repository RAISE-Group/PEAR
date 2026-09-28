@cache_readonly
def is_unique_asi8(self):
    return len(self.deltas_asi8) == 1