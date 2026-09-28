@pytest.mark.parametrize('t', ['float16', 'float32', 'float64', 'int32', 'int64'])
def test_astype(self, t):
    mgr = create_mgr('c: f4; d: f2; e: f8')
    t = np.dtype(t)
    tmgr = mgr.astype(t)
    assert tmgr.get('c').dtype.type == t
    assert tmgr.get('d').dtype.type == t
    assert tmgr.get('e').dtype.type == t
    mgr = create_mgr('a,b: object; c: bool; d: datetime; e: f4; f: f2; g: f8')
    t = np.dtype(t)
    tmgr = mgr.astype(t, errors='ignore')
    assert tmgr.get('c').dtype.type == t
    assert tmgr.get('e').dtype.type == t
    assert tmgr.get('f').dtype.type == t
    assert tmgr.get('g').dtype.type == t
    assert tmgr.get('a').dtype.type == np.object_
    assert tmgr.get('b').dtype.type == np.object_
    if t != np.int64:
        assert tmgr.get('d').dtype.type == np.datetime64
    else:
        assert tmgr.get('d').dtype.type == t