@pytest.mark.parametrize('index,val', [(Index([0, 1, '2']), 0), (Index([0, 1, '2']), '2')])
def test_mixed_index_contains(self, index, val):
    assert val in index