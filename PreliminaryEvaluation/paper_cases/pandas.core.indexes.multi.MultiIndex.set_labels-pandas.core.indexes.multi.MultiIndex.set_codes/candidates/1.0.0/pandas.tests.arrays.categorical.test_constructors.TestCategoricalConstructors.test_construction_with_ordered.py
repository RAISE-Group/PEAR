@pytest.mark.parametrize('ordered', [None, True, False])
def test_construction_with_ordered(self, ordered):
    cat = Categorical([0, 1, 2], ordered=ordered)
    assert cat.ordered == bool(ordered)