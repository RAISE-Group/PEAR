def test_unstack_multiple_hierarchical(self):
    df = DataFrame(index=[[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]], columns=[[0, 0, 1, 1], [0, 1, 0, 1]])
    df.index.names = ['a', 'b', 'c']
    df.columns.names = ['d', 'e']
    df.unstack(['b', 'c'])