def test_searchsorted(self):
    for o in self.objs:
        index = np.searchsorted(o, max(o))
        assert 0 <= index <= len(o)
        index = np.searchsorted(o, max(o), sorter=range(len(o)))
        assert 0 <= index <= len(o)