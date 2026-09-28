def test_to_records_index_name(self):
    df = DataFrame(np.random.randn(3, 3))
    df.index.name = 'X'
    rs = df.to_records()
    assert 'X' in rs.dtype.fields
    df = DataFrame(np.random.randn(3, 3))
    rs = df.to_records()
    assert 'index' in rs.dtype.fields
    df.index = MultiIndex.from_tuples([('a', 'x'), ('a', 'y'), ('b', 'z')])
    df.index.names = ['A', None]
    rs = df.to_records()
    assert 'level_0' in rs.dtype.fields