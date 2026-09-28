def test_copy(self):
    off = self._offset(weekmask='Mon Wed Fri')
    assert off == off.copy()