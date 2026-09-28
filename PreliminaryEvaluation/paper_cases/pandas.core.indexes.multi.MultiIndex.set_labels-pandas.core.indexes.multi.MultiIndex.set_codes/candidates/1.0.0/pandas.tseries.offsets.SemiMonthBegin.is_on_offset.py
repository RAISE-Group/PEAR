def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    return dt.day in (1, self.day_of_month)