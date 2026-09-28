def __getitem__(self, item):
    if isinstance(item, numbers.Integral):
        return self.data[item]
    else:
        return type(self)(self.data[item])