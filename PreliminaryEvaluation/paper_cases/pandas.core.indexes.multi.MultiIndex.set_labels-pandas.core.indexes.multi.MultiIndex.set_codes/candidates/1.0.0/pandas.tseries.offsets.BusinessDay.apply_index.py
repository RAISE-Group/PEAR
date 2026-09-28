@apply_index_wraps
def apply_index(self, i):
    time = i.to_perioddelta('D')
    asper = i.to_period('B')
    if not isinstance(asper._data, np.ndarray):
        asper = asper._data
    if self.n > 0:
        shifted = (i.to_perioddelta('B') - time).asi8 != 0
        roll = np.where(shifted, self.n - 1, self.n)
        shifted = asper._addsub_int_array(roll, operator.add)
    else:
        roll = self.n
        shifted = asper._time_shift(roll)
    result = shifted.to_timestamp() + time
    return result