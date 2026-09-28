def test_min_max(self):
    cat = Series(Categorical(['a', 'b', 'c', 'd'], ordered=False))
    with pytest.raises(TypeError):
        cat.min()
    with pytest.raises(TypeError):
        cat.max()
    cat = Series(Categorical(['a', 'b', 'c', 'd'], ordered=True))
    _min = cat.min()
    _max = cat.max()
    assert _min == 'a'
    assert _max == 'd'
    cat = Series(Categorical(['a', 'b', 'c', 'd'], categories=['d', 'c', 'b', 'a'], ordered=True))
    _min = cat.min()
    _max = cat.max()
    assert _min == 'd'
    assert _max == 'a'
    cat = Series(Categorical([np.nan, 'b', 'c', np.nan], categories=['d', 'c', 'b', 'a'], ordered=True))
    _min = cat.min()
    _max = cat.max()
    assert _min == 'c'
    assert _max == 'b'
    cat = Series(Categorical([np.nan, 1, 2, np.nan], categories=[5, 4, 3, 2, 1], ordered=True))
    _min = cat.min()
    _max = cat.max()
    assert _min == 2
    assert _max == 1