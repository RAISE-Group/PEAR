def copy(self):
    return type(self)(self.data[:])