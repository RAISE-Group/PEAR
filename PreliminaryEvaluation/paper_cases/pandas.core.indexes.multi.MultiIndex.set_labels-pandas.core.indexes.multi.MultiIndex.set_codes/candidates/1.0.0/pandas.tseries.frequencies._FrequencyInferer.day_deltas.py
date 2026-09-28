@cache_readonly
def day_deltas(self):
    return [x / _ONE_DAY for x in self.deltas]