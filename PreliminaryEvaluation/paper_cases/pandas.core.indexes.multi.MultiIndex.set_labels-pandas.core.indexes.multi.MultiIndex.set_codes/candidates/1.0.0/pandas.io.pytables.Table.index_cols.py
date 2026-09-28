def index_cols(self):
    """ return a list of my index cols """
    return [(i.axis, i.cname) for i in self.index_axes]