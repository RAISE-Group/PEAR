def __eq__(self, other: Any) -> bool:
    if isinstance(other, str):
        try:
            other = self.construct_from_string(other)
        except TypeError:
            return False
    if isinstance(other, type(self)):
        subtype = self.subtype == other.subtype
        if self._is_na_fill_value:
            fill_value = other._is_na_fill_value and isinstance(self.fill_value, type(other.fill_value)) or isinstance(other.fill_value, type(self.fill_value))
        else:
            fill_value = self.fill_value == other.fill_value
        return subtype and fill_value
    return False