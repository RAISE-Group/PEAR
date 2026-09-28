def values_cols(self) -> List[str]:
    """ return a list of my values cols """
    return [i.cname for i in self.values_axes]