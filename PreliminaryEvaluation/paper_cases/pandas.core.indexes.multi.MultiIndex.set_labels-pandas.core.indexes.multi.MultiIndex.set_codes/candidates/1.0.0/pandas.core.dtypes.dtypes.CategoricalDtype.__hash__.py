def __hash__(self) -> int:
    if self.categories is None:
        if self.ordered:
            return -1
        else:
            return -2
    return int(self._hash_categories(self.categories, self.ordered))