def setup_method(self, _):
    self.lst = [1, 2, 3, 4, 5]
    self.container = FrozenList(self.lst)