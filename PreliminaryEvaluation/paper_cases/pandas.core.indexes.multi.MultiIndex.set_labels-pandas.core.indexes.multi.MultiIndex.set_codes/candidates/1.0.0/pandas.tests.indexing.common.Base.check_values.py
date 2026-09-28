def check_values(self, f, func, values=False):
    if f is None:
        return
    axes = f.axes
    indicies = itertools.product(*axes)
    for i in indicies:
        result = getattr(f, func)[i]
        if values:
            expected = f.values[i]
        else:
            expected = f
            for a in reversed(i):
                expected = expected.__getitem__(a)
        tm.assert_almost_equal(result, expected)