@pytest.mark.parametrize('index,val', [(Index([0, 1, '2']), '1'), (Index([0, 1, '2']), 2)])
def test_mixed_index_not_contains(self, index, val):
    assert val not in index