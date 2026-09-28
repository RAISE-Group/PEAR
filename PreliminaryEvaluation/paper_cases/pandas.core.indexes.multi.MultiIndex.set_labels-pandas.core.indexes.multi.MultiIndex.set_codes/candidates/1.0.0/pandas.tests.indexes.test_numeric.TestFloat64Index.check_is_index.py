def check_is_index(self, i):
    assert isinstance(i, Index)
    assert not isinstance(i, Float64Index)