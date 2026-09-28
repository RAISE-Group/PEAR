@property
def nseries(self):
    if self.data.ndim == 1:
        return 1
    else:
        return self.data.shape[1]