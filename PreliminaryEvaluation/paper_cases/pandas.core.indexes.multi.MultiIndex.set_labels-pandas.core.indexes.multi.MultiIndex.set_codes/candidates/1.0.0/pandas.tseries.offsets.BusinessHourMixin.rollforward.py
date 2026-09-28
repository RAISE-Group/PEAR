@apply_wraps
def rollforward(self, dt):
    """
        Roll provided date forward to next offset only if not on offset.
        """
    if not self.is_on_offset(dt):
        if self.n >= 0:
            return self._next_opening_time(dt)
        else:
            return self._prev_opening_time(dt)
    return dt