@pytest.mark.skipif(PYPY, reason='not relevant for PyPy')
def test_memory_usage(self):
    delegate = self.Delegate(self.Delegator())
    sys.getsizeof(delegate)