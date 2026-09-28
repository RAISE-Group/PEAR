@apply_index_wraps
def apply_index(self, i):
    shifted = liboffsets.shift_months(i.asi8, self.n, self._day_opt)
    return type(i)._simple_new(shifted, freq=i.freq, dtype=i.dtype)