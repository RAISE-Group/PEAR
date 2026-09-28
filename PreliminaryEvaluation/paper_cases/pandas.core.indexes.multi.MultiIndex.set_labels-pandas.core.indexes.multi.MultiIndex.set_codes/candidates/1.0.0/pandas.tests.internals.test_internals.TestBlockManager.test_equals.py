def test_equals(self):
    bm1 = create_mgr('a,b,c: i8-1; d,e,f: i8-2')
    bm2 = BlockManager(bm1.blocks[::-1], bm1.axes)
    assert bm1.equals(bm2)
    bm1 = create_mgr('a,a,a: i8-1; b,b,b: i8-2')
    bm2 = BlockManager(bm1.blocks[::-1], bm1.axes)
    assert bm1.equals(bm2)