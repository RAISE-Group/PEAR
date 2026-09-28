def is_anchored(self):
    return self.n == 1 and self.startingMonth is not None and (self.weekday is not None)