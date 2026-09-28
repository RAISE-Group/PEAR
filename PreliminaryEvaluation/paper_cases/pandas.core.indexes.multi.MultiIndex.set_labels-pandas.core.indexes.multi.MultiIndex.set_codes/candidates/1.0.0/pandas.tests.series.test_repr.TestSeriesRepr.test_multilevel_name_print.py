def test_multilevel_name_print(self):
    index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['first', 'second'])
    s = Series(range(len(index)), index=index, name='sth')
    expected = ['first  second', 'foo    one       0', '       two       1', '       three     2', 'bar    one       3', '       two       4', 'baz    two       5', '       three     6', 'qux    one       7', '       two       8', '       three     9', 'Name: sth, dtype: int64']
    expected = '\n'.join(expected)
    assert repr(s) == expected