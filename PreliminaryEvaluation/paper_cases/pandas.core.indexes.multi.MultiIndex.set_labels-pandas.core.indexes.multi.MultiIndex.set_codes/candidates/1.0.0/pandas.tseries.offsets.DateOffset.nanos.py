@property
def nanos(self):
    raise ValueError(f'{self} is a non-fixed frequency')