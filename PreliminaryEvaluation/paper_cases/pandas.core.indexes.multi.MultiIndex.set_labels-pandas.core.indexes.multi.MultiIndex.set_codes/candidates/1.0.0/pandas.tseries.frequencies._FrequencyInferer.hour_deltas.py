@cache_readonly
def hour_deltas(self):
    return [x / _ONE_HOUR for x in self.deltas]