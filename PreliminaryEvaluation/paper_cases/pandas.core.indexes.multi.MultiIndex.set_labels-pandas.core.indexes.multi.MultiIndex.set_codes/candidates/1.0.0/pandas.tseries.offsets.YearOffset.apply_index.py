@apply_index_wraps
def apply_index(self, dtindex):
    shifted = liboffsets.shift_quarters(dtindex.asi8, self.n, self.month, self._day_opt, modby=12)
    return type(dtindex)._simple_new(shifted, freq=dtindex.freq, dtype=dtindex.dtype)