@pytest.mark.skipif(compat.is_platform_32bit(), reason='GH 23440')
def test_construction_overflow(self):
    left, right = (np.arange(101, dtype='int64'), [np.iinfo(np.int64).max] * 101)
    tree = IntervalTree(left, right)
    result = tree.root.pivot
    expected = (50 + np.iinfo(np.int64).max) / 2
    assert result == expected