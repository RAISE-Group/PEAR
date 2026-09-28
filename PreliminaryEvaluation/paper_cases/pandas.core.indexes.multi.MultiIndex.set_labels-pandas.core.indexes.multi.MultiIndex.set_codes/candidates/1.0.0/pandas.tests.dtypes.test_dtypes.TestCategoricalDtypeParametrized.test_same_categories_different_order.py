def test_same_categories_different_order(self):
    c1 = CategoricalDtype(['a', 'b'], ordered=True)
    c2 = CategoricalDtype(['b', 'a'], ordered=True)
    assert c1 is not c2