def _convert_obj(self, obj):
    obj = super()._convert_obj(obj)
    if self._from_selection:
        msg = 'Resampling from level= or on= selection with a PeriodIndex is not currently supported, use .set_index(...) to explicitly set index'
        raise NotImplementedError(msg)
    if self.loffset is not None:
        self.kind = 'timestamp'
    if self.kind == 'timestamp':
        obj = obj.to_timestamp(how=self.convention)
    return obj