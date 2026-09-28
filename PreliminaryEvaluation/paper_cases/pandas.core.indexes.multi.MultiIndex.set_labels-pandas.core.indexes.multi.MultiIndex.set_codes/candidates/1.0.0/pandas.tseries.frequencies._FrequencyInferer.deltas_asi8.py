@cache_readonly
def deltas_asi8(self):
    return unique_deltas(self.index.asi8)