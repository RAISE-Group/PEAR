@pytest.mark.parametrize('sort', [None, False])
def test_union2(self, sort):
    everything = tm.makeDateIndex(10)
    first = everything[:5]
    second = everything[5:]
    union = first.union(second, sort=sort)
    tm.assert_index_equal(union, everything)