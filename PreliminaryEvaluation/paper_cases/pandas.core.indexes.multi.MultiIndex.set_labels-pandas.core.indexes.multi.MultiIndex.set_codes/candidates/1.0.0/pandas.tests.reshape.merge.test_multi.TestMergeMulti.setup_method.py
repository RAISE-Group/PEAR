def setup_method(self):
    self.index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['first', 'second'])
    self.to_join = DataFrame(np.random.randn(10, 3), index=self.index, columns=['j_one', 'j_two', 'j_three'])
    key1 = ['bar', 'bar', 'bar', 'foo', 'foo', 'baz', 'baz', 'qux', 'qux', 'snap']
    key2 = ['two', 'one', 'three', 'one', 'two', 'one', 'two', 'two', 'three', 'one']
    data = np.random.randn(len(key1))
    self.data = DataFrame({'key1': key1, 'key2': key2, 'data': data})