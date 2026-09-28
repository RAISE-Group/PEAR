def is_anchored(self):
    return self.n == 1 and self._offset.is_anchored()