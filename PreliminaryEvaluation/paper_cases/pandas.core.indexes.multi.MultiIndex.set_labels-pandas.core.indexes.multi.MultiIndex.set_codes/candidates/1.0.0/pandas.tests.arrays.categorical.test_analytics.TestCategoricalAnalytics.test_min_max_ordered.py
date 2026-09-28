def test_min_max_ordered(self):
    cat = Categorical(['a', 'b', 'c', 'd'], ordered=True)
    _min = cat.min()
    _max = cat.max()
    assert _min == 'a'
    assert _max == 'd'
    cat = Categorical(['a', 'b', 'c', 'd'], categories=['d', 'c', 'b', 'a'], ordered=True)
    _min = cat.min()
    _max = cat.max()
    assert _min == 'd'
    assert _max == 'a'