def _check_all_fields(self, periodindex):
    fields = ['year', 'month', 'day', 'hour', 'minute', 'second', 'weekofyear', 'week', 'dayofweek', 'dayofyear', 'quarter', 'qyear', 'days_in_month']
    periods = list(periodindex)
    s = pd.Series(periodindex)
    for field in fields:
        field_idx = getattr(periodindex, field)
        assert len(periodindex) == len(field_idx)
        for x, val in zip(periods, field_idx):
            assert getattr(x, field) == val
        if len(s) == 0:
            continue
        field_s = getattr(s.dt, field)
        assert len(periodindex) == len(field_s)
        for x, val in zip(periods, field_s):
            assert getattr(x, field) == val