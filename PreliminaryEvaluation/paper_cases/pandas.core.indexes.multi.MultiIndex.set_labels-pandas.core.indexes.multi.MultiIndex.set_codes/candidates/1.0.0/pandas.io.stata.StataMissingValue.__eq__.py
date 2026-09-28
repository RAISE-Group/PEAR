def __eq__(self, other: Any) -> bool:
    return isinstance(other, type(self)) and self.string == other.string and (self.value == other.value)