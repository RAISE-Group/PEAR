def test_deepcopy_empty(self):
    empty_frame = DataFrame(data=[], index=[], columns=['A'])
    empty_frame_copy = deepcopy(empty_frame)
    self._compare(empty_frame_copy, empty_frame)