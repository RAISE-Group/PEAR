def test_set_change_dtype(self, mgr):
    mgr.set('baz', np.zeros(N, dtype=bool))
    mgr.set('baz', np.repeat('foo', N))
    assert mgr.get('baz').dtype == np.object_
    mgr2 = mgr.consolidate()
    mgr2.set('baz', np.repeat('foo', N))
    assert mgr2.get('baz').dtype == np.object_
    mgr2.set('quux', tm.randn(N).astype(int))
    assert mgr2.get('quux').dtype == np.int_
    mgr2.set('quux', tm.randn(N))
    assert mgr2.get('quux').dtype == np.float_