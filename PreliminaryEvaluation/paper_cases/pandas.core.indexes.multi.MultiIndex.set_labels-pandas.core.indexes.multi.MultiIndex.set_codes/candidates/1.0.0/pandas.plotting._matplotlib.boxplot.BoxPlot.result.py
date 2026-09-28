@property
def result(self):
    if self.return_type is None:
        return super().result
    else:
        return self._return_obj