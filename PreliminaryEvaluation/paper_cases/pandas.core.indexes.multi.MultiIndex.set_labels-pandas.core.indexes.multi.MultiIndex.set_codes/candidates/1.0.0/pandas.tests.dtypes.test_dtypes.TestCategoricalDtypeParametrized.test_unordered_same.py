@pytest.mark.parametrize('ordered', [False, None])
def test_unordered_same(self, ordered):
    c1 = CategoricalDtype(['a', 'b'], ordered=ordered)
    c2 = CategoricalDtype(['b', 'a'], ordered=ordered)
    assert hash(c1) == hash(c2)