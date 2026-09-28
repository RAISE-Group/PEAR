def test_mixed_type_join_with_suffix(self):
    df = DataFrame(np.random.randn(20, 6), columns=['a', 'b', 'c', 'd', 'e', 'f'])
    df.insert(0, 'id', 0)
    df.insert(5, 'dt', 'foo')
    grouped = df.groupby('id')
    mn = grouped.mean()
    cn = grouped.count()
    mn.join(cn, rsuffix='_right')