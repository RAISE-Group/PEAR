def items(self):
    """
        iterate on key->group
        """
    for g in self.groups():
        yield (g._v_pathname, g)