def test_items(self):
    cols = ['a', 'b', 'c']
    df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=cols)
    for c, (k, v) in zip(cols, df.items()):
        assert c == k
        assert isinstance(v, Series)
        assert (df[k] == v).all()