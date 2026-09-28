def _get_grouper(self, obj, validate: bool=True):
    r = self._get_resampler(obj)
    r._set_binner()
    return (r.binner, r.grouper, r.obj)