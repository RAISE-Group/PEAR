@cache_readonly
def slabels(self):
    return algorithms.take_nd(self.labels, self.sort_idx, allow_fill=False)