def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    if type(self) == DateOffset or isinstance(self, Tick):
        return True
    a = dt
    b = dt + self - self
    return a == b