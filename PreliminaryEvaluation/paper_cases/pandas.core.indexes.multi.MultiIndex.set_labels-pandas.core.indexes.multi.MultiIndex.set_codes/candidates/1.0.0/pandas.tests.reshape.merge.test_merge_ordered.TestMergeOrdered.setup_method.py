def setup_method(self, method):
    self.left = DataFrame({'key': ['a', 'c', 'e'], 'lvalue': [1, 2.0, 3]})
    self.right = DataFrame({'key': ['b', 'c', 'd', 'f'], 'rvalue': [1, 2, 3.0, 4]})