def test_is_monotonic(self):
    index = self._holder([1, 2, 3, 4])
    assert index.is_monotonic is True
    assert index.is_monotonic_increasing is True
    assert index._is_strictly_monotonic_increasing is True
    assert index.is_monotonic_decreasing is False
    assert index._is_strictly_monotonic_decreasing is False
    index = self._holder([4, 3, 2, 1])
    assert index.is_monotonic is False
    assert index._is_strictly_monotonic_increasing is False
    assert index._is_strictly_monotonic_decreasing is True
    index = self._holder([1])
    assert index.is_monotonic is True
    assert index.is_monotonic_increasing is True
    assert index.is_monotonic_decreasing is True
    assert index._is_strictly_monotonic_increasing is True
    assert index._is_strictly_monotonic_decreasing is True