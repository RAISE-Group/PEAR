def test_cumprod(self, datetime_series):
    _check_accum_op('cumprod', datetime_series)