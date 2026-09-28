def test_mixed(self):
    a = CategoricalDtype(['a', 'b', 1, 2])
    b = CategoricalDtype(['a', 'b', '1', '2'])
    assert hash(a) != hash(b)