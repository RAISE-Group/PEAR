@pytest.mark.parametrize('comp', [Index(['a', 'b']), Index(['a', 'b', 'd']), ['a', 'b', 'c']])
def test_not_equals_object(self, comp):
    assert not Index(['a', 'b', 'c']).equals(comp)