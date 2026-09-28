def test_create_index_existing_name(self):
    expected = self.create_index()
    if not isinstance(expected, MultiIndex):
        expected.name = 'foo'
        result = pd.Index(expected)
        tm.assert_index_equal(result, expected)
        result = pd.Index(expected, name='bar')
        expected.name = 'bar'
        tm.assert_index_equal(result, expected)
    else:
        expected.names = ['foo', 'bar']
        result = pd.Index(expected)
        tm.assert_index_equal(result, Index(Index([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('baz', 'two'), ('qux', 'one'), ('qux', 'two')], dtype='object'), names=['foo', 'bar']))
        result = pd.Index(expected, names=['A', 'B'])
        tm.assert_index_equal(result, Index(Index([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('baz', 'two'), ('qux', 'one'), ('qux', 'two')], dtype='object'), names=['A', 'B']))