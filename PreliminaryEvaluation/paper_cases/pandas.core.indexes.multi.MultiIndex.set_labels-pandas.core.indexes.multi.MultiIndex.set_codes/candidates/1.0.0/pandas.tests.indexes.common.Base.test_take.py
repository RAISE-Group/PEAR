def test_take(self, indices):
    indexer = [4, 3, 0, 2]
    if len(indices) < 5:
        return
    result = indices.take(indexer)
    expected = indices[indexer]
    assert result.equals(expected)
    if not isinstance(indices, (DatetimeIndex, PeriodIndex, TimedeltaIndex)):
        with pytest.raises(AttributeError):
            indices.freq