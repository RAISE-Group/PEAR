@pytest.mark.skipif(PYPY, reason='not relevant for PyPy')
def test_memory_usage(self):
    for o in self.objs:
        res = o.memory_usage()
        res_deep = o.memory_usage(deep=True)
        if is_object_dtype(o) or (isinstance(o, Series) and is_object_dtype(o.index)):
            assert res_deep > res
        else:
            assert res == res_deep
        if isinstance(o, Series):
            assert o.memory_usage(index=False) + o.index.memory_usage() == o.memory_usage(index=True)
        diff = res_deep - sys.getsizeof(o)
        assert abs(diff) < 100