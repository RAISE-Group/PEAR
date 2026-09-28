def fillna(self, value, limit=None, inplace=False, downcast=None):
    if self._can_hold_element(value):
        return super().fillna(value, limit, inplace, downcast)
    return self.astype(object).fillna(value, limit=limit, inplace=inplace, downcast=downcast)