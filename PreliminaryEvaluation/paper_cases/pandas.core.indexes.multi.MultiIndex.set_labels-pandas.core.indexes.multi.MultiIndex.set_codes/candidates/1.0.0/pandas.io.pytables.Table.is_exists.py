@property
def is_exists(self) -> bool:
    """ has this table been created """
    return 'table' in self.group