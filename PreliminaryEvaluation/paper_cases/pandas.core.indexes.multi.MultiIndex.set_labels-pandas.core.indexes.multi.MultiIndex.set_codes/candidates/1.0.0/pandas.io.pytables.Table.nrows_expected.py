@property
def nrows_expected(self) -> int:
    """ based on our axes, compute the expected nrows """
    return np.prod([i.cvalues.shape[0] for i in self.index_axes])