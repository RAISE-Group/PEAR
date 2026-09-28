@pytest.mark.parametrize('order', (list(x) for x in permutations(range(3))))
def test_is_overlapping_endpoints(self, closed, order):
    """shared endpoints are marked as overlapping"""
    left, right = (np.arange(3, dtype='int64'), np.arange(1, 4))
    tree = IntervalTree(left[order], right[order], closed=closed)
    result = tree.is_overlapping
    expected = closed == 'both'
    assert result is expected