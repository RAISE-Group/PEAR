def test_lookup_basics(self):

    def _check(index):
        assert index.lookup(0) == -1
        assert index.lookup(5) == 0
        assert index.lookup(7) == 2
        assert index.lookup(8) == -1
        assert index.lookup(9) == -1
        assert index.lookup(10) == -1
        assert index.lookup(11) == -1
        assert index.lookup(12) == 3
        assert index.lookup(17) == 8
        assert index.lookup(18) == -1
    bindex = BlockIndex(20, [5, 12], [3, 6])
    iindex = bindex.to_int_index()
    _check(bindex)
    _check(iindex)