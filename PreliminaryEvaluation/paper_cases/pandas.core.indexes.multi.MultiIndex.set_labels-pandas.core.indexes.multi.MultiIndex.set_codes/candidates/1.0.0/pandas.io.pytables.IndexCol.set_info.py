def set_info(self, info):
    """ set my state from the passed info """
    idx = info.get(self.name)
    if idx is not None:
        self.__dict__.update(idx)