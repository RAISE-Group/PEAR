def __invert__(self):
    if not self.size:
        return self
    arr = operator.inv(com.values_from_object(self))
    return self.__array_wrap__(arr)