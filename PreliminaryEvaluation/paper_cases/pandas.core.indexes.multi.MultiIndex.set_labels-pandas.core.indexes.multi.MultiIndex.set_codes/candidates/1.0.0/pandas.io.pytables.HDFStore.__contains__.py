def __contains__(self, key: str) -> bool:
    """ check for existence of this key
              can match the exact pathname or the pathnm w/o the leading '/'
              """
    node = self.get_node(key)
    if node is not None:
        name = node._v_pathname
        if name == key or name[1:] == key:
            return True
    return False