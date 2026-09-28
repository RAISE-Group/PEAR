def test_contains(self, mgr):
    assert 'a' in mgr
    assert 'baz' not in mgr