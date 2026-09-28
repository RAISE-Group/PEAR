@cache_readonly
def _engine(self):
    sizes = np.ceil(np.log2([len(l) + 1 for l in self.levels]))
    lev_bits = np.cumsum(sizes[::-1])[::-1]
    offsets = np.concatenate([lev_bits[1:], [0]]).astype('uint64')
    if lev_bits[0] > 64:
        return MultiIndexPyIntEngine(self.levels, self.codes, offsets)
    return MultiIndexUIntEngine(self.levels, self.codes, offsets)