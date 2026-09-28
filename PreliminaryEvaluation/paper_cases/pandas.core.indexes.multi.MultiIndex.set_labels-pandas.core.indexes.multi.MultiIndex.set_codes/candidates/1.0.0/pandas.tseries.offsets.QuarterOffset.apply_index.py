@apply_index_wraps
def apply_index(self, dtindex):
    shifted = liboffsets.shift_quarters(dtindex.asi8, self.n, self.startingMonth, self._day_opt)
    return type(dtindex)._simple_new(shifted, freq=dtindex.freq, dtype=dtindex.dtype)