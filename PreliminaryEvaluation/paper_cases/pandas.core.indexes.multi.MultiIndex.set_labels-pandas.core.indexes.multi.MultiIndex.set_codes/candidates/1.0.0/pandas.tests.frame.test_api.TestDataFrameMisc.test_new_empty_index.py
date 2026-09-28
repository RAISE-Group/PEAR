def test_new_empty_index(self):
    df1 = DataFrame(np.random.randn(0, 3))
    df2 = DataFrame(np.random.randn(0, 3))
    df1.index.name = 'foo'
    assert df2.index.name is None