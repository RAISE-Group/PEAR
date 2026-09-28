def _combine_match_index(self, other, func):
    if ops.should_series_dispatch(self, other, func):
        new_data = ops.dispatch_to_series(self, other, func)
    else:
        with np.errstate(all='ignore'):
            new_data = func(self.values.T, other.values).T
    return new_data