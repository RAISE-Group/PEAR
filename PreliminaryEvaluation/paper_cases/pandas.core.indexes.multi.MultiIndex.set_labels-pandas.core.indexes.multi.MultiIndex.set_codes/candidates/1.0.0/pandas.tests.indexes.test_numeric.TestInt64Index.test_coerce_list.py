def test_coerce_list(self):
    arr = Index([1, 2, 3, 4])
    assert isinstance(arr, Int64Index)
    arr = Index([1, 2, 3, 4], dtype=object)
    assert isinstance(arr, Index)