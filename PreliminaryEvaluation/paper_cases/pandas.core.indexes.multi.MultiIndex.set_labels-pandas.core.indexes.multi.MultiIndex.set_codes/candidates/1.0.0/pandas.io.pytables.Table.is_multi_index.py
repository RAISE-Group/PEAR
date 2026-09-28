@property
def is_multi_index(self) -> bool:
    """the levels attribute is 1 or a list in the case of a multi-index"""
    return isinstance(self.levels, list)