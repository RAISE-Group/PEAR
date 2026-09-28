def test_equal_but_different(self, ordered_fixture):
    c1 = CategoricalDtype([1, 2, 3])
    c2 = CategoricalDtype([1.0, 2.0, 3.0])
    assert c1 is not c2
    assert c1 != c2