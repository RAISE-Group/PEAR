def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    if dt.tzinfo is not None:
        dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
    return self._is_on_offset(dt)