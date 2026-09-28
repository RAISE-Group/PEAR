def test_get(self):
    cols = Index(list('abc'))
    values = np.random.rand(3, 3)
    block = make_block(values=values.copy(), placement=np.arange(3))
    mgr = BlockManager(blocks=[block], axes=[cols, np.arange(3)])
    tm.assert_almost_equal(mgr.get('a').internal_values(), values[0])
    tm.assert_almost_equal(mgr.get('b').internal_values(), values[1])
    tm.assert_almost_equal(mgr.get('c').internal_values(), values[2])