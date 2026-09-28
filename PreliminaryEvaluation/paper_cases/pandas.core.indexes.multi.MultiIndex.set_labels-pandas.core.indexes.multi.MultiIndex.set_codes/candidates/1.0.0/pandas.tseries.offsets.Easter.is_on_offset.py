def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    return date(dt.year, dt.month, dt.day) == easter(dt.year)