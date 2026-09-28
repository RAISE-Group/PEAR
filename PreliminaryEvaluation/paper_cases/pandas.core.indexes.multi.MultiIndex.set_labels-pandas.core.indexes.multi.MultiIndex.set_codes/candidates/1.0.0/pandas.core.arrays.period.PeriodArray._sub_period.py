def _sub_period(self, other):
    self._check_compatible_with(other)
    asi8 = self.asi8
    new_data = asi8 - other.ordinal
    new_data = np.array([self.freq * x for x in new_data])
    if self._hasnans:
        new_data[self._isnan] = NaT
    return new_data