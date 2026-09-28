def test_bad_take(self):
    with pytest.raises(IndexError, match='bounds'):
        self.arr.take([11])