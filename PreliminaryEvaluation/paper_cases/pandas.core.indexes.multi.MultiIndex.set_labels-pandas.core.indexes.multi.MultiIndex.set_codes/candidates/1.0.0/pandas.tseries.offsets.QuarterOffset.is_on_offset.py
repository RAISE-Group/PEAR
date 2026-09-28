def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    mod_month = (dt.month - self.startingMonth) % 3
    return mod_month == 0 and dt.day == self._get_offset_day(dt)