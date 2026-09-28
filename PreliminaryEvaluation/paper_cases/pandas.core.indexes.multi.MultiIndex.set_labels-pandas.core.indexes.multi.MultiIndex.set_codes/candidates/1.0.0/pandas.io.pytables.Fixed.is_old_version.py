@property
def is_old_version(self) -> bool:
    return self.version[0] <= 0 and self.version[1] <= 10 and (self.version[2] < 1)