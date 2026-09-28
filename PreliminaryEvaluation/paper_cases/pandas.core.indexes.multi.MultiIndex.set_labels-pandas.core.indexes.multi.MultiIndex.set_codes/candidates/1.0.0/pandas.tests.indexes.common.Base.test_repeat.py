def test_repeat(self):
    rep = 2
    i = self.create_index()
    expected = pd.Index(i.values.repeat(rep), name=i.name)
    tm.assert_index_equal(i.repeat(rep), expected)
    i = self.create_index()
    rep = np.arange(len(i))
    expected = pd.Index(i.values.repeat(rep), name=i.name)
    tm.assert_index_equal(i.repeat(rep), expected)