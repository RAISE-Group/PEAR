def _getitem_scalar(self, key):
    values = self.obj._get_value(*key)
    return values