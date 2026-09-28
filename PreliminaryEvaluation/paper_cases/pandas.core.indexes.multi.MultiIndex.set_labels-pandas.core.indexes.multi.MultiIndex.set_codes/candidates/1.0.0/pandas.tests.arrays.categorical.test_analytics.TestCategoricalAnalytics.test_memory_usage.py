def test_memory_usage(self):
    cat = Categorical([1, 2, 3])
    assert 0 < cat.nbytes <= cat.memory_usage()
    assert 0 < cat.nbytes <= cat.memory_usage(deep=True)
    cat = Categorical(['foo', 'foo', 'bar'])
    assert cat.memory_usage(deep=True) > cat.nbytes
    if not PYPY:
        diff = cat.memory_usage(deep=True) - sys.getsizeof(cat)
        assert abs(diff) < 100