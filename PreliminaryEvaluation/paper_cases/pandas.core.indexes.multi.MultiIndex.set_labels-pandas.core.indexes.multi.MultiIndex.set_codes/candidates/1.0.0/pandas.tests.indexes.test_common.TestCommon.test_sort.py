def test_sort(self, indices):
    msg = 'cannot sort an Index object in-place, use sort_values instead'
    with pytest.raises(TypeError, match=msg):
        indices.sort()