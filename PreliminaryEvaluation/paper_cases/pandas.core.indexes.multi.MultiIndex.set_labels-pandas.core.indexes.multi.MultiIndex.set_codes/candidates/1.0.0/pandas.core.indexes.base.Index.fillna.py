@Appender(_index_shared_docs['fillna'])
def fillna(self, value=None, downcast=None):
    self._assert_can_do_op(value)
    if self.hasnans:
        result = self.putmask(self._isnan, value)
        if downcast is None:
            return Index(result, name=self.name)
    return self._shallow_copy()