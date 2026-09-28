def test_truncate_copy(self, datetime_frame):
    index = datetime_frame.index
    truncated = datetime_frame.truncate(index[5], index[10])
    truncated.values[:] = 5.0
    assert not (datetime_frame.values[5:11] == 5).any()