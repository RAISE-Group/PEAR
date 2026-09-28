def __add__(self, other):
    if isinstance(other, Tick):
        if type(self) == type(other):
            return type(self)(self.n + other.n)
        else:
            return _delta_to_tick(self.delta + other.delta)
    elif isinstance(other, Period):
        return other + self
    try:
        return self.apply(other)
    except ApplyTypeError:
        return NotImplemented
    except OverflowError:
        raise OverflowError(f'the add operation between {self} and {other} will overflow')