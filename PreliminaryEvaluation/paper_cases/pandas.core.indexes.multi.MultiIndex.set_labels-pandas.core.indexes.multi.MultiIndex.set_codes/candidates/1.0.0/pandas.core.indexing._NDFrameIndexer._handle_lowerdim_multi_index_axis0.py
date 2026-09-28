def _handle_lowerdim_multi_index_axis0(self, tup: Tuple):
    axis = self.axis or 0
    try:
        return self._get_label(tup, axis=axis)
    except TypeError:
        pass
    except KeyError as ek:
        if len(tup) <= self.obj.index.nlevels and len(tup) > self.ndim:
            raise ek
    return None