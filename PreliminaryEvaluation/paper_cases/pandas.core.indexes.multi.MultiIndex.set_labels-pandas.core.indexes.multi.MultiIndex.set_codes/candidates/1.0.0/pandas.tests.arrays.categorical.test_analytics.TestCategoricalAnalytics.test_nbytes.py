def test_nbytes(self):
    cat = Categorical([1, 2, 3])
    exp = 3 + 3 * 8
    assert cat.nbytes == exp