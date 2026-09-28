@apply_wraps
def rollback(self, dt):
    """
        Roll provided date backward to next offset only if not on offset.
        """
    if not self.is_on_offset(dt):
        if self.n >= 0:
            dt = self._prev_opening_time(dt)
        else:
            dt = self._next_opening_time(dt)
        return self._get_closing_time(dt)
    return dt