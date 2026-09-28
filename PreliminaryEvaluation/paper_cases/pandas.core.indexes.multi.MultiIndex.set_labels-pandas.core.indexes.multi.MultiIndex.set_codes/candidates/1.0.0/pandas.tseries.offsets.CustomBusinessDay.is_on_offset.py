def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    day64 = _to_dt64(dt, 'datetime64[D]')
    return np.is_busday(day64, busdaycal=self.calendar)