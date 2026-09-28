def _searchsorted_monotonic(self, label, side='left'):
    if self.is_monotonic_increasing:
        return self.searchsorted(label, side=side)
    elif self.is_monotonic_decreasing:
        pos = self[::-1].searchsorted(label, side='right' if side == 'left' else 'left')
        return len(self) - pos
    raise ValueError('index must be monotonic increasing or decreasing')