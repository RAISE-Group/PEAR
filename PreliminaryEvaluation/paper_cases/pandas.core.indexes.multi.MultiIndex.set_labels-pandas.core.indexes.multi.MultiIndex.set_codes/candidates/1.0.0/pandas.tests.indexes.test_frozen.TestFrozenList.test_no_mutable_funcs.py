def test_no_mutable_funcs(self):

    def setitem():
        self.container[0] = 5
    self.check_mutable_error(setitem)

    def setslice():
        self.container[1:2] = 3
    self.check_mutable_error(setslice)

    def delitem():
        del self.container[0]
    self.check_mutable_error(delitem)

    def delslice():
        del self.container[0:3]
    self.check_mutable_error(delslice)
    mutable_methods = ('extend', 'pop', 'remove', 'insert')
    for meth in mutable_methods:
        self.check_mutable_error(getattr(self.container, meth))