def __eq__(self, other: Any) -> bool:
    """ compare 2 col items """
    return all((getattr(self, a, None) == getattr(other, a, None) for a in ['name', 'cname', 'axis', 'pos']))