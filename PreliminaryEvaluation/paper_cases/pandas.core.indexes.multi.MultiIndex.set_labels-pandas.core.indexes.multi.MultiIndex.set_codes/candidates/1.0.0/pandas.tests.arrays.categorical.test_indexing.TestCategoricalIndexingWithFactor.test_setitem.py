def test_setitem(self):
    c = self.factor.copy()
    c[0] = 'b'
    assert c[0] == 'b'
    c[-1] = 'a'
    assert c[-1] == 'a'
    c = self.factor.copy()
    indexer = np.zeros(len(c), dtype='bool')
    indexer[0] = True
    indexer[-1] = True
    c[indexer] = 'c'
    expected = Categorical(['c', 'b', 'b', 'a', 'a', 'c', 'c', 'c'], ordered=True)
    tm.assert_categorical_equal(c, expected)