@cache_readonly
def deltas(self):
    return unique_deltas(self.values)