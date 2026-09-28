def test_monotonic(self, closed):
    idx = IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)], closed=closed)
    assert idx.is_monotonic is True
    assert idx._is_strictly_monotonic_increasing is True
    assert idx.is_monotonic_decreasing is False
    assert idx._is_strictly_monotonic_decreasing is False
    idx = IntervalIndex.from_tuples([(4, 5), (2, 3), (1, 2)], closed=closed)
    assert idx.is_monotonic is False
    assert idx._is_strictly_monotonic_increasing is False
    assert idx.is_monotonic_decreasing is True
    assert idx._is_strictly_monotonic_decreasing is True
    idx = IntervalIndex.from_tuples([(0, 1), (4, 5), (2, 3)], closed=closed)
    assert idx.is_monotonic is False
    assert idx._is_strictly_monotonic_increasing is False
    assert idx.is_monotonic_decreasing is False
    assert idx._is_strictly_monotonic_decreasing is False
    idx = IntervalIndex.from_tuples([(0, 2), (0.5, 2.5), (1, 3)], closed=closed)
    assert idx.is_monotonic is True
    assert idx._is_strictly_monotonic_increasing is True
    assert idx.is_monotonic_decreasing is False
    assert idx._is_strictly_monotonic_decreasing is False
    idx = IntervalIndex.from_tuples([(1, 3), (0.5, 2.5), (0, 2)], closed=closed)
    assert idx.is_monotonic is False
    assert idx._is_strictly_monotonic_increasing is False
    assert idx.is_monotonic_decreasing is True
    assert idx._is_strictly_monotonic_decreasing is True
    idx = IntervalIndex.from_tuples([(0.5, 2.5), (0, 2), (1, 3)], closed=closed)
    assert idx.is_monotonic is False
    assert idx._is_strictly_monotonic_increasing is False
    assert idx.is_monotonic_decreasing is False
    assert idx._is_strictly_monotonic_decreasing is False
    idx = pd.IntervalIndex.from_tuples([(1, 2), (1, 3), (2, 3)], closed=closed)
    assert idx.is_monotonic is True
    assert idx._is_strictly_monotonic_increasing is True
    assert idx.is_monotonic_decreasing is False
    assert idx._is_strictly_monotonic_decreasing is False
    idx = pd.IntervalIndex.from_tuples([(2, 3), (1, 3), (1, 2)], closed=closed)
    assert idx.is_monotonic is False
    assert idx._is_strictly_monotonic_increasing is False
    assert idx.is_monotonic_decreasing is True
    assert idx._is_strictly_monotonic_decreasing is True
    idx = IntervalIndex.from_tuples([(0, 1), (0, 1)], closed=closed)
    assert idx.is_monotonic is True
    assert idx._is_strictly_monotonic_increasing is False
    assert idx.is_monotonic_decreasing is True
    assert idx._is_strictly_monotonic_decreasing is False
    idx = IntervalIndex([], closed=closed)
    assert idx.is_monotonic is True
    assert idx._is_strictly_monotonic_increasing is True
    assert idx.is_monotonic_decreasing is True
    assert idx._is_strictly_monotonic_decreasing is True