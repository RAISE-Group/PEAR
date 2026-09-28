def test_transpose(self):
    for obj in self.objs:
        tm.assert_equal(obj.transpose(), obj)