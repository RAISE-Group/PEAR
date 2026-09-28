def assert_series_equal(self, left, right, *args, **kwargs):

    def convert(x):
        try:
            return math.isnan(x)
        except TypeError:
            return False
    if left.dtype == 'object':
        left_na = left.apply(convert)
    else:
        left_na = left.isna()
    if right.dtype == 'object':
        right_na = right.apply(convert)
    else:
        right_na = right.isna()
    tm.assert_series_equal(left_na, right_na)
    return tm.assert_series_equal(left[~left_na], right[~right_na], *args, **kwargs)