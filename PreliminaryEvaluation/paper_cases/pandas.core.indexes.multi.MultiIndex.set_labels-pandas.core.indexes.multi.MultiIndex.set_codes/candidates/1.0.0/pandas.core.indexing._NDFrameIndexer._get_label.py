def _get_label(self, label, axis: int):
    if self.ndim == 1:
        return self.obj._xs(label, axis=axis)
    elif isinstance(label, tuple) and isinstance(label[axis], slice):
        raise IndexingError('no slices here, handle elsewhere')
    return self.obj._xs(label, axis=axis)