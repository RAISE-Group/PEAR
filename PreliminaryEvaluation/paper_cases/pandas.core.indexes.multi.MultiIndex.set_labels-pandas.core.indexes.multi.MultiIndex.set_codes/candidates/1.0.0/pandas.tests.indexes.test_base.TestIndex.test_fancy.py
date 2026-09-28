def test_fancy(self):
    index = self.create_index()
    sl = index[[1, 2, 3]]
    for i in sl:
        assert i == sl[sl.get_loc(i)]