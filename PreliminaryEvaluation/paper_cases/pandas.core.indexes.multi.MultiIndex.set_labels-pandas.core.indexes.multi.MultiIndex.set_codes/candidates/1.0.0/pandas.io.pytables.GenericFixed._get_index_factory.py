def _get_index_factory(self, klass):
    if klass == DatetimeIndex:

        def f(values, freq=None, tz=None):
            result = DatetimeIndex._simple_new(values.values, name=None, freq=freq)
            if tz is not None:
                result = result.tz_localize('UTC').tz_convert(tz)
            return result
        return f
    elif klass == PeriodIndex:

        def f(values, freq=None, tz=None):
            return PeriodIndex._simple_new(values, name=None, freq=freq)
        return f
    return klass