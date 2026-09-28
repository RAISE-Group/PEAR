def test_attrs(self):
    mgr = create_mgr('a,b,c: f8-1; d,e,f: f8-2')
    assert mgr.nblocks == 2
    assert len(mgr) == 6