def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    elif self.weekday is None:
        return True
    return dt.weekday() == self.weekday