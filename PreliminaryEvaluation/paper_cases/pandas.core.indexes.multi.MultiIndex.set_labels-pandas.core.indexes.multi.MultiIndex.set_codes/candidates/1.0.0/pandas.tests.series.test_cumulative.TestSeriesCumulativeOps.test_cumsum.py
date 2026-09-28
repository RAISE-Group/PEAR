def test_cumsum(self, datetime_series):
    _check_accum_op('cumsum', datetime_series)