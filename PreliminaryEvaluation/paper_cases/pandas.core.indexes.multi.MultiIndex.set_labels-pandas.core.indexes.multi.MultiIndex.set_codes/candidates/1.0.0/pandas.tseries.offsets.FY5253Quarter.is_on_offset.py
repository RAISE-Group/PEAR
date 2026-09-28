def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    if self._offset.is_on_offset(dt):
        return True
    next_year_end = dt - self._offset
    qtr_lens = self.get_weeks(dt)
    current = next_year_end
    for qtr_len in qtr_lens:
        current = liboffsets.shift_day(current, days=qtr_len * 7)
        if dt == current:
            return True
    return False