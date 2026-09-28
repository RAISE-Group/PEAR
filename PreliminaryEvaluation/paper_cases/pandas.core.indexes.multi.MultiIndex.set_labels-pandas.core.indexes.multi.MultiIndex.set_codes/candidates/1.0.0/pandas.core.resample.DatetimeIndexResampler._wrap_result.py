def _wrap_result(self, result):
    result = super()._wrap_result(result)
    if self.kind == 'period' and (not isinstance(result.index, PeriodIndex)):
        result.index = result.index.to_period(self.freq)
    return result