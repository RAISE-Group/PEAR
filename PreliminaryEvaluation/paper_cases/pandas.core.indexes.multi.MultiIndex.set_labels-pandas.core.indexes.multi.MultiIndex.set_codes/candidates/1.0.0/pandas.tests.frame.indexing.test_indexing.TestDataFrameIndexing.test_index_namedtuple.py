def test_index_namedtuple(self):
    from collections import namedtuple
    IndexType = namedtuple('IndexType', ['a', 'b'])
    idx1 = IndexType('foo', 'bar')
    idx2 = IndexType('baz', 'bof')
    index = Index([idx1, idx2], name='composite_index', tupleize_cols=False)
    df = DataFrame([(1, 2), (3, 4)], index=index, columns=['A', 'B'])
    result = df.loc[IndexType('foo', 'bar')]['A']
    assert result == 1