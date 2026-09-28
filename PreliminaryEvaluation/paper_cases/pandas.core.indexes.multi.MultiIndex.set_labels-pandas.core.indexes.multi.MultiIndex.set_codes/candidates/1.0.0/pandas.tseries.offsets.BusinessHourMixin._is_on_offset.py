def _is_on_offset(self, dt):
    """
        Slight speedups using calculated values.
        """
    if self.n >= 0:
        op = self._prev_opening_time(dt)
    else:
        op = self._next_opening_time(dt)
    span = (dt - op).total_seconds()
    businesshours = 0
    for i, st in enumerate(self.start):
        if op.hour == st.hour and op.minute == st.minute:
            businesshours = self._get_business_hours_by_sec(st, self.end[i])
    if span <= businesshours:
        return True
    else:
        return False